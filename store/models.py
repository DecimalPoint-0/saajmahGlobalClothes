from django.db import models
from django.utils.text import slugify


class Size(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Color(models.Model):
    name = models.CharField(max_length=50)
    hex = models.CharField(max_length=7, blank=True)

    def __str__(self):
        return self.name


class Costume(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220, unique=True, blank=True)
    description = models.TextField(blank=True)
    age_range = models.CharField(max_length=80, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    available = models.BooleanField(default=True)
    # optional primary image; additional images are in CostumeImage
    image = models.ImageField(upload_to='costumes/', blank=True, null=True)
    sizes = models.ManyToManyField(Size, blank=True, related_name='costumes')
    colors = models.ManyToManyField(Color, blank=True, related_name='costumes')

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('processing', 'Processing'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]

    costume = models.ForeignKey(Costume, on_delete=models.PROTECT, related_name='orders')
    size = models.ForeignKey(Size, null=True, blank=True, on_delete=models.SET_NULL)
    color = models.ForeignKey(Color, null=True, blank=True, on_delete=models.SET_NULL)
    customer_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=30, blank=True)
    organization = models.CharField(max_length=200, blank=True)
    quantity = models.PositiveIntegerField(default=1)
    date_from = models.DateField(null=True, blank=True)
    date_to = models.DateField(null=True, blank=True)
    notes = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Order #{self.pk} — {self.customer_name} ({self.costume.name})"



class CostumeImage(models.Model):
    costume = models.ForeignKey(Costume, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='costume_images/')
    alt_text = models.CharField(max_length=200, blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"Image for {self.costume.name} ({self.pk})"
