from typing import Any
from django.forms import ModelForm
from main.models import Product
from django.utils.html import strip_tags

class GetSupplyForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'description', 'image']
        
    def clean_product(self):
        product = self.cleaned_data.get('product')
        return strip_tags(product)
    
    def clean_price(self):
        price = self.cleaned_data.get('price')
        return strip_tags(price)
