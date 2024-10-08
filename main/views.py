from django.shortcuts import render, redirect, reverse
from main.forms import GetSupplyForm
from main.models import Product
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
import datetime
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils.html import strip_tags

@login_required(login_url='/login')
def show_products(request):
    content = {
        'user_name': request.user.username,
        'name' : 'Rafif Sulaiman Dirvesa',
        'npm' : "2306222771",
        'class' : 'PBP C',
        'last_login' : request.COOKIES['last_login'],
    }
    
    return render(request, 'main.html', content)

def create_supply(request):
    form = GetSupplyForm(request.POST, request.FILES or None)
    if form.is_valid() and request.method == 'POST':
        supply_entry = form.save(commit=False)
        supply_entry.user = request.user
        supply_entry.save()
        return redirect('main:show_products')
    
    context = {"form": form}
    return render(request, 'create_supply.html', context)

def show_xml(request):
    data = Product.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Product.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def register(request):
    form = UserCreationForm()
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('main:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_products"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.error(request, 'Username atau password salah!')

    else:
        form = AuthenticationForm(request)
    context = {'form': form}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def edit_product(request, id):
    #get product entry berdasarkan id
    product = Product.objects.get(pk = id)

    # Set product entry sebagai instance dari form
    form = GetSupplyForm(request.POST or None, instance=product)

    if form.is_valid() and request.method == "POST":
        # Simpan form dan kembali ke halaman awal
        form.save()
        return HttpResponseRedirect(reverse('main:show_products'))

    context = {'form': form}
    return render(request, "edit_product.html", context)

def delete_product(request, id):
    product = Product.objects.get(pk = id)
    product.delete()
    return HttpResponseRedirect(reverse('main:show_products'))

@csrf_exempt
@require_POST
def add_product_ajax(request):
    form = GetSupplyForm(request.POST, request.FILES or None)
    if form.is_valid():
        supply_entry = form.save(commit=False)
        supply_entry.user = request.user
        supply_entry.save()
        return JsonResponse({'message': 'Product added successfully!'}, status=201)
    else:
        return JsonResponse({'errors': form.errors}, status=400)