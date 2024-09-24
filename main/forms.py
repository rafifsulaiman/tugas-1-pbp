from django.forms import ModelForm
from main.models import Product

class GetSupplyForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'description', 'image']