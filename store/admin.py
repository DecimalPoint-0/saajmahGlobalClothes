from django.contrib import admin
from .models import Costume, Order, CostumeImage, Size, Color


class CostumeImageInline(admin.TabularInline):
    model = CostumeImage
    extra = 1


@admin.register(Costume)
class CostumeAdmin(admin.ModelAdmin):
    list_display = ('name', 'age_range', 'price', 'available')
    prepopulated_fields = {'slug': ('name',)}
    inlines = [CostumeImageInline]
    filter_horizontal = ('sizes', 'colors')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer_name', 'costume', 'size', 'color', 'quantity', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('customer_name', 'email', 'phone')


@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ('name', 'hex')
