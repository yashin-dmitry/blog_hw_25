from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    FORBIDDEN_WORDS = ['bad', 'evil', 'harmful']

    class Meta:
        model = Product
        fields = '__all__'

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if any(word in name.lower() for word in self.FORBIDDEN_WORDS):
            raise forms.ValidationError("Name contains forbidden words.")
        return name

    def clean_description(self):
        description = self.cleaned_data.get('description')
        if any(word in description.lower() for word in self.FORBIDDEN_WORDS):
            raise forms.ValidationError("Description contains forbidden words.")
        return description

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price < 0:
            raise forms.ValidationError("Price cannot be negative.")
        return price
