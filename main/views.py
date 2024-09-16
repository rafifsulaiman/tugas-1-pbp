from django.shortcuts import render, redirect
from main.forms import GetSupplyForm
from main.models import Product
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_products(request):
    product_entries = Product.objects.all()
    content = {
        'name' : 'Ultra Milk 1 L Full Cream',
        'price' : 20000,
        'description' : 'Ultra milk 1L full cream with plain flavor',
        'image' : 'https://i.imgur.com/Xe74ORV.jpeg',
        'product_entries' : product_entries,
    }
    
    return render(request, 'main.html', content)

def create_supply(request):
    form = GetSupplyForm(request.POST or None)
    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect('main:show_products')
    
    context = {"form": form}
    return render(request, 'create_supply.html', context)

def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")