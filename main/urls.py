from main.views import show_products, create_supply, show_json, show_json_by_id, show_xml, show_xml_by_id, register, login_user, logout_user, edit_product, delete_product, add_product_ajax, create_product_flutter
from django.urls import path

app_name = 'main'
urlpatterns = [
    path('', show_products, name='show_products'),
    path('create-supply', create_supply, name='create_supply'),
    path('json/', show_json, name='show_json'),
    path('json/<str:id>', show_json_by_id, name='show_json_by_id'),
    path('xml/', show_xml, name='show_xml'),
    path('xml/<str:id>', show_xml_by_id, name='show_xml_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('edit-product/<uuid:id>', edit_product, name='edit_product'),
    path('delete-product/<uuid:id>', delete_product, name='delete_product'),
    path('add-product-ajax', add_product_ajax, name='add_product_ajax'),
    path('create-flutter/', create_product_flutter, name='create_product_flutter'),
]