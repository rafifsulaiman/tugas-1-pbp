from django.shortcuts import render

# Create your views here.
def show_products(request):
    content = {
        'name' : 'Ultra Milk 1 L Full Cream',
        'price' : 20000,
        'description' : 'Ultra milk 1L full cream with plain flavor',
        'image' : 'https://i.imgur.com/Xe74ORV.jpeg',
        'person_name' : 'Rafif Sulaiman Dirvesa',
        'person_class' : 'PBP C',
        'person_npm' : '2306222771'
    }

    return render(request, 'main.html', content)