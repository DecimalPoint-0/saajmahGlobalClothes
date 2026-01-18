from django import forms
from .models import Order, Size, Color


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['customer_name', 'email', 'phone', 'organization', 'quantity', 'size', 'color', 'date_from', 'date_to', 'notes']
        widgets = {
            'date_from': forms.DateInput(attrs={'type': 'date', 'class': 'input'}),
            'date_to': forms.DateInput(attrs={'type': 'date', 'class': 'input'}),
            'notes': forms.Textarea(attrs={'rows': 3, 'class': 'input'}),
        }

    def __init__(self, *args, **kwargs):
        # accept 'costume' to limit size/color choices to those available for that costume
        costume = kwargs.pop('costume', None)
        super().__init__(*args, **kwargs)
        self.fields['customer_name'].widget.attrs.update({'class': 'input'})
        self.fields['email'].widget.attrs.update({'class': 'input'})
        self.fields['phone'].widget.attrs.update({'class': 'input'})
        self.fields['organization'].widget.attrs.update({'class': 'input'})
        self.fields['quantity'].widget.attrs.update({'class': 'input', 'min': '1'})
        # default to all sizes/colors, but prefer costume-specific choices when available
        self.fields['size'].queryset = Size.objects.all()
        self.fields['color'].queryset = Color.objects.all()
        if costume:
            if costume.sizes.exists():
                self.fields['size'].queryset = costume.sizes.all()
            if costume.colors.exists():
                self.fields['color'].queryset = costume.colors.all()
        # set a friendly empty label for ModelChoiceFields so users see a prompt
        if hasattr(self.fields['size'], 'empty_label'):
            self.fields['size'].empty_label = 'Select size'
        if hasattr(self.fields['color'], 'empty_label'):
            self.fields['color'].empty_label = 'Select color'
        # add classes to size/color selects
        self.fields['size'].widget.attrs.update({'class': 'input'})
        self.fields['color'].widget.attrs.update({'class': 'input'})
