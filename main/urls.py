from main.views import show_products
from django.urls import path

app_name = 'main'
urlpatterns = [
    path('', show_products, name='show_products'),
]