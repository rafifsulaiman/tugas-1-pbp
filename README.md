# GetSupply
## Personal Data

- Nama : Rafif Sulaiman Dirvesa
- NPM : 2306222771
- Kelas : PBP C
- Link PWS: http://rafif-sulaiman-getsupply.pbp.cs.ui.ac.id/
#

# Table of Contents
- [Tugas 2](#tugas-2)
- [Tugas 3](#tugas-3)
- [Tugas 4](#tugas-4)
- [Tugas 5](#tugas-5)

# TUGAS 2
[Back to Table of Contents](#table-of-contents)
## Jawaban
1. untuk membuat sebuah proyek Django baru, saya membuat direktori baru pada file explorer saya, lalu membuka command prompt dan memasukkan perintah ```-m venv env```, lalu menuliskan perintah ```env\Scripts\activate```. ketika env sudah aktif, saya membuat requirements.txt berisikan dependencies-dependencies yang diperlukan, lalu melakukan perintah pada command prompt berupa ```pip install -r requirements.txt```, lalu melakukan deactivate.

- lalu, kita membuat proyek django dengan menjalankan perintah ```django-admin startproject get_supply```. perintah tersebut berfungsi untuk membuat folder berdasarkan nama proyek saya dan sudah berisi file-file bawaan proyek dari django. setelah itu, saya menjalankan perintah python ```manage.py``` startapp main pada command prompt direktori proyek saya. perintah tersebut berfungsi untuk membuat folder main berisikan template-template bawaan dari Django pada direktori proyek saya.

- lalu, saya menambahkan main ke dalam INSTALLED_APPS pada file ```settings.py``` bawaan Django. main yang dimaksud adalah file main.html yang terbuat ketika saya memulai proyek Django pada direktori proyek saya.

- lalu pada berkas ```models.py```, saya menambahkan class Product berisikan atribut-atribut yang menggunakan fungsi bawaan dari class Model pada Django. atribut-atribut yang saya definisikan adalah name, price, dan description yang diwajibkan serta saya menambahkan atribut baru untuk mempercantik tampilan berisikan gambar yang saya namakan image. berikut bentuk class dan atribut yang saya buat.
```bash
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=300)
    price = models.IntegerField()
    description = models.TextField(max_length=300)
    image = models.ImageField() #upload image
```

- setelah saya membuat atribut pada ```models.py```, saya membuat dictionary yang berisikan data yang akan saya masukkan kedalam template HTML. data yang diperlukan saya letakkan pada file ```views.py``` dan berisikan seperti berikut.
```bash
from django.shortcuts import render

def show_products(request):
    content = {
        'name' : 'Ultra Milk 1 L Full Cream',
        'price' : 20000,
        'description' : 'Ultra milk 1L full cream with plain flavor',
        'image' : 'https://i.imgur.com/Xe74ORV.jpeg'
    }

    return render(request, 'main.html', content)
```

- ```return render(request, 'main.html', content)``` berfungsi untuk mengantar isi dari dictionary content ke template HTML yang sudah saya buat, berikut isi dari template HTML-nya.

```bash
<h1>Welcome to GetSupply by Rafif Sulaiman Dirvesa/2306222771</h1>

<h5>Name: </h5>
<p>{{ name }}</p>
<h5>Price: </h5>
<p>{{ price }}</p>
<h5>Description: </h5>
<p>{{ description }}</p>
<img src="{{ image }}">
```

- untuk melakukan pemetakan fungsi yang telah dibuat pada ```views.py```, saya membuat routing sebagai berikut.
```bash
from main.views import show_products
from django.urls import path

app_name = 'main'
urlpatterns = [
    path('', show_products, name='show_products'),
]
```

- setelah saya selesai membuat proyek, saya membuat repo baru dengan visibilitas public pada akun github saya untuk melakukan upload ke dalam github. pertama-tama, saya melakukan perintah ```git init``` pada command prompt direktori proyek saya, membuat branch baru dengan perintah ```git checkout -b main```, melakukan add, commit, dan push, diakhiri dengan menjalankan perintah ```git push -u origin main``` (nama branch).

- untuk melakukan upload pada PWS, saya membuka halaman PWS pada https://pbp.cs.ui.ac.id dan melakukan login. lalu saya membuat proyek baru pada PWS dengan menekan tombol Create New Project dan menamai proyeknya dengan tugas-1-pbp. lalu saya membuka kembali file ```settings.py``` saya dan menambahkan URL deployment PWS saya pada ALLOWED_HOST dengan format <username-sso>-<nama proyek>.pbp.cs.ui.ac.id dan melakukan git add, commit, dan push ke Github. lalu saya mengikuti tahapan-tahapan berupa perintah command prompt yang terdapat pada Project Command pada halaman PWS proyek saya. terakhir saya melakukan perintah pada command prompt berupa git branch -M main untuk mengubah branch utama menjadi main.

2. berikut bagan berisi request client ke web aplikasi berbasis Django.
![messageImage_1725905119582](https://github.com/user-attachments/assets/5dc1c04a-a684-48a3-8a75-fb18979ed9d7)

ketika ada HTTP request yang dilakukan melalui browsing platform, alamat HTTP akan dicek apakah sesuai dengan url yang berada pada file ```urls.py```. jika sesuai, maka permintaan akan dilanjutkan ke file ```views.py``` yang berisikan data untuk atribut-atribut yang terdapat pada ```models.py```. setelah mendapatkan data dan juga atribut, data dan atribut itu akan disalurkan ke template yang sudah dibuat dengan file main.html. setelah data masuk ke dalam template, template akan memberikan respon ke browsing platform dengan menyajikan tampilan web sesuai dengan template yang sudah dibuat.

4. git dapat menyimpan riwayat perubahan pada kode pengguna dan kembali ke versi sebelumnya, memfasilitasi kolaborasi tim pada proyek yang dikerjakan bersama, dan memungkinkan pengguna untuk membuat dan mengelola berbagai versi proyek.

5. karena framework django sangat ramah untuk dipelajari pemula, menyediakan banyak fitur built-in, dan memiliki banyak paket tambahan dan alat yang dapat memperluas fungsionalitasnya.

6. Model pada Django disebut ORM (Object-Relational Mapping) karena Django memungkinkan pengguna untuk berinteraksi dengan basis data menggunakan kode Python. ORM ini menyediakan cara untuk mendefinisikan model basis data menggunakan kelas Python dan secara otomatis menghasilkan petnyataan SQL untuk berinteraksi dengan basisi data berdasarkan model tersebut.


# TUGAS 3
[Back to Table of Contents](#table-of-contents)
## Jawaban
**1. Manfaat Data Delivery**

Data delivery diperlukan untuk memastikan bahwa data yang diproses oleh backend (server dan database) dapat terkirim ke frontend (antarmuka pengguna) untuk ditampilkan kepada pengguna. selain itu, data delivery yang efisien membantu memberikan pengalaman kepada pengguna dengan baik. misal jika pengguna mengisi suatu form, platform harus segera memberikan tanggapan apakah data berhasil diproses atau ada kesalahan.

referensi: https://docs.djangoproject.com/en/4.0/ref/request-response/#jsonresponse-objects

**2. Perbandingan JSON dan XML**

Menurut saya JSON lebih baik daripada XML dan alasan saya berpikir seperti itu serta kenapa JSON lebih populer ketimbang XML dikarenakan beberapa hal berikut:

- JSON memiliki struktur yang lebih sederhana dan lebih mudah dibaca ketimbang XML. Hal ini dikarenakan JSON menggunakan format pasangan key-value pada objeknya.

contoh JSON:
```bash
{
  "name": "John",
  "age": 30,
  "city": "New York"
}
```

contoh XML:
```bash
<person>
  <name>John</name>
  <age>30</age>
  <city>New York</city>
</person>
```

- JSON memiliki ukuran data yang lebih ringan dibandingkan dengan XML. Hal ini dikarenakan JSON tidak memerlukan tag pembuka dan penutup seperti XML. Struktur yang lebih ringkas ini membuat JSON lebih efisien dalam hal ukuran ketimbang XML.

- Secara alami, JSON didukung oleh sebagian besar bahasa pemrograman modern, terutama JavaScript. Hal ini menyebabkan parsing JSON menggunakan JavaScript lebih mudah, begitu juga dengan bahasa-bahasa pemrograman lain, ada library bawaan yang mendukung JSON secara efisien.

referensi: https://www.geeksforgeeks.org/difference-between-json-and-xml/

**3. Fungsi dari method ```is_valid()```**

Method ```is_valid()``` pada form Django adalah metode yang berfungsi untuk melakukan validasi pada data yang dimasukkan oleh penguna melalui form. Method ini digunakan untuk memeriksa apakah data yang dikirim ke form sesuai dengan aturan validasi yang telah ditentukan, seperti batasan panjang pada data, tipe data, dan lain-lain.

referensi: https://docs.djangoproject.com/en/5.1/ref/forms/validation/

**4. Fungsi ```csrf_token```**

Kita membutuhkan ```csrf_token``` untuk melindungi form yang telah dibuat dari serangan CSRF (Cross-Site Request Forgery), yaitu serangan yang dilakukan dengan memalsukan permintaan yang terlihat sah menggunakan sesi pengguna yang sedang aktif. Jika token ini tidak ditambahkan, penyerang dapat mengirim permintaan tanpa izin, seperti mengubah data atau melakukan transaksi atas nama pengguna. Dengan token ini, setiap form di Django memiliki token unik yang diverifikasi oleh server, sehingga jika token tidak ada atau tidak valid, permintaan akan ditolak sehingga serangan CSRF dapat dicegah.

referensi: https://docs.djangoproject.com/en/5.1/ref/csrf/

**5. Berikut penjelasan step-by-step bagaimana cara saya mengimplementasikan checklist yang diminta.**
- Pertama-tama, saya membuat direktori baru bernama ```templates``` pada root project, lalu membuat file ```base.html``` yang berguna untuk dijadikan sebagai template dasar atau kerangka umum untuk halaman web lainnya.
```bash
{% load static %}
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    {% block meta %} {% endblock meta %}
  </head>

  <body>
    {% block content %} {% endblock content %}
  </body>
</html>
```

- Lalu saya menambah data pada variabel ```TEMPLATES``` pada file ```settings.py``` saya.
```bash
...
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        ...
    }
]
...
```

- Kemudian, saya memodifikasi file ```main.html``` saya agar melakukan ekstensi ```base.html```.
```bash
{% extends 'base.html' %}
{% block content %}
<h1>Welcome to GetSupply</h1>
...
```

- Lalu, saya menambahkan atribut id yang menggunakan UUID field pada ```models.py``` saya.
```bash
import uuid

class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    ...
```

- Setelah menambah variabel pada ```models.py```, saya melakukan migrasi
- lalu, saya membuat file ```forms.py``` pada direktori ```main``` yang berfungsi sebagai tempat menerima data product baru. 
```bash
from django.forms import ModelForm
from main.models import Product

class GetSupplyForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'description']
```

- lalu saya melakukan beberapa modifikasi pada ```views.py``` saya untuk dapat mengakses file ```forms.py```, membuat fungsi ```create_supply``` untuk menerima request, dan menambahkan variabel pada ```show_products```.
```bash
from django.shortcuts import render, redirect
from main.forms import GetSupplyForm
from main.models import Product
from django.http import HttpResponse
from django.core import serializers

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
```

- lalu, saya menambahkan path untuk ```create_supply``` pada file ```urls.py``` saya dengan melakukan import ```create_supply```
```bash
urlpatterns = [
    ...
    path('create-supply', create_supply, name='create_supply'),
]
```

- lalu saya membuat file baru bernama ```create_supply``` yang berfungsi sebagai template pada tampilan web saya ketika melakukan input data product.
```bash
{% extends 'base.html' %} 
{% block content %}
<h1>Add New Product</h1>

<form method="POST">
  {% csrf_token %}
  <table>
    {{ form.as_table }}
    <tr>
      <td></td>
      <td>
        <input type="submit" value="Add Product" />
      </td>
    </tr>
  </table>
</form>

{% endblock %}
``` 

- kemudian saya memodifikasi file ```main.html``` saya dengan menambahkan bagian untuk menampilkan data product yang sudah di input serta memunculkan tombol "Add New Product" yang akan redirect ke halaman form.
```bash
{% extends 'base.html' %}
{% block content %}
<h1>Welcome to GetSupply</h1>
<p> By: Rafif Sulaiman Dirvesa/PBP C/2306222771

<h5>Name: </h5>
<p>{{ name }}</p>
<h5>Price: </h5>
<p>{{ price }}</p>
<h5>Description: </h5>
<p>{{ description }}</p>
<img src="{{ image }}">

{% if not product_entries %}
<p>Belum ada data produk pada GetSupply.</p>
{% else %}
<table>
  <tr>
    <th>Product Name</th>
    <th>Price</th>
    <th>Description</th>
  </tr>

  {% for product_entry in product_entries %}
  <tr>
    <td>{{product_entry.name}}</td>
    <td>{{product_entry.price}}</td>
    <td>{{product_entry.description}}</td>
  </tr>
  {% endfor %}
</table>
{% endif %}

<br />

<a href="{% url 'main:create_supply' %}">
  <button>Add New product</button>
</a>
{% endblock content %}
```

- lalu, saya memodifikasi file ```views.py``` saya untuk dapat menampilkan data dalam format JSON dan XML, serta menampilkan data dalam format JSON dan XML berdasarkan IDnya.
```bash
from django.shortcuts import render, redirect
from main.forms import GetSupplyForm
from main.models import Product
from django.http import HttpResponse
from django.core import serializers

...

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
```

# Screenshot Postman
[Back to Table of Contents](#table-of-contents)

**show_xml**
![Screenshot (24)](https://github.com/user-attachments/assets/b5a65ea4-d7c5-43ef-92c8-8f97d72a5dea)

**show_json**
![Screenshot (25)](https://github.com/user-attachments/assets/f78b5a6f-063a-42b0-8b79-9f4c39641e6d)

**show_xml_by_id**
![Screenshot (26)](https://github.com/user-attachments/assets/0758f734-fc87-4a55-973b-3199ff6c7805)

**show_json_by_id**
![Screenshot (27)](https://github.com/user-attachments/assets/a1cd74bb-a63a-42f3-9b92-b4a87913e64e)


# TUGAS 4
[Back to Table of Contents](#table-of-contents)
## Jawaban
**1. Apa perbedaan antara ```HttpResponseRedirect()``` dan ```redirect()```**

```HttpResponseRedirect()``` dan ```redirect()``` merupakan 2 cara untuk melakukan pengalihan (redirect) dalam Django, namun ada beberapa perbedaan dalam cara menggunakannya, yaitu:

- ```HttpResponseRedirect()``` adalah funsgi ntuk melakukan pengalihan yang perlu diberikan URL lengkap atau relatif sebagai argumen, seperti ```return HttpResponseRedirect('/url/')```. Untuk ini, perlu membangun URL sendiri,sehingga lebih rumit jika URL memerlukan penggunaan fungsi pembalik URL (reverse).

- ```redirect()``` adalah fungsi yang menyediakan cara yang lebih mudah dan fleksibel untuk melakukan pengalihan. Fungsi ini dapat menerima URL, model instance, atau bahkan nama tampilan sebagai argumen, contohnya ```return redirect('view_name', arg1='value')```. Fungsi ini juga mendukung penggunaan fungsi pembalik (```reverse()```) untuk membangun URL dari nama tampilan, sehingga lebih mudah dan fleksibel dalam penggunaannya.

**2. Berikut langkah-langkah cara kerja penghubungan model Product dengan User**
- Tambahkan field ```ForeignKey``` pada model ```Product``` yang mengarah ke model ```User```.
```bash
from django.db import models
import uuid
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_name = models.CharField(max_length=255)
    ...
```
- ```User``` pada ```Product``` membuat hubungan antara entry product dan pengguna yang membuat product tersebut. Fungsi ```on_delete=models.CASCADE``` adalah agar ketika ```User``` dihapus, maka entry pada ```Product``` yang terkait juga akan terhapus. Satu ```User``` dapat memiliki banyak ```Product```, tetapi tiap ```Product``` hanya bisa dimiliki oleh satu ```User```. Saat membuat ```Product``` baru, entry tersebut dapat dihubungkan dengan pengguna yang sedang login dan membuat entry tersebut.

```bash
def create_supply(request):
    form = GetSupplyForm(request.POST, request.FILES or None)
    if form.is_valid() and request.method == 'POST':
        supply_entry = form.save(commit=False)
        supply_entry.user = request.user
        supply_entry.save()
        return redirect('main:show_products')
    
    context = {"form": form}
    return render(request, 'create_supply.html', context)
```
- Melalui kode diatas, ```Product``` akan terhubung dengan ```User``` yang membuat entry tersebut menggunakan ```ForeignKey``` user. Penghubungan ini memungkinkan server untuk melacak product setiap pengguna dan mengelola data secara terpisah berdasarkan pengguna yang login.


**3. Perbedaan antara Authentication dan Authorization:**

- Authentication adalah suatu proses untuk memverifikasi identitas pengguna dan memastikan apakah akun pengguna terdapat pada sistem, tujuannya adalah untuk menentukan siapa pengguna tersebut. Biasanya melibatkan pemeriksaan kredensial seperti username/password, token, dan metode autentikasi lainnya.

- Authorization adalah suatu proses untuk menentukan apa yang dapat dilakukan oleh pengguna yang sudah terautentikasi. Bertujuan untuk menentukan apa yang diizinkan dan tidak diizinkan bagi pengguna.

**Proses yang terjadi saat pengguna login**
- Pengguna memasukkan data kredensial (username dan password).
- Django melakukan verifikasi kredensial tersebut terhadap data yang ada pada basis data.
- Jika data kredensial cocok, Django akan mengidentifikasi pengguna sebagai pengguna yang valid dan sesi autentikasi dimulai.
- Pengguna yang dianggap sudah terautentikasi dapat melanjutkan ke bagian lain dari aplikasi sesuai dengan otorisasi yang akan menetukan akses mereka.

**Implementasi Authentication dan Authorization pada Django**

Authentication di Django
- Django menggunakan sistem autentikasi bawaan seperti login, logout, dan manajemen sesi pengguna
- Modul yang digunakan adalah ```django.contrib.auth``` yang menyediakan model User, sistem login dan logout, serta autentikasi
- Django juga mendukung autentikasi berbasis token, OAuth, dan metode autentikasi pihak ketiga melalui pustaka seperti ```django-allauth``` dan ```djangorestframework```

Authorization di Django
- Django mengelola otorisasi menggunakan permissions yang dapat diatur pada model, URL, atau tampilan tertentu
- Permissions diatur dengan menggunakan dekorator seperti ```@login_required```
- Django juga menyediakan pembatasan akses berbasis grup atau peran pengguna

**4. Bagaimana Django mengingat pengguna yang telah login?**
- Django menggunakan cookies dan session untuk menghubungkan pengguna dengan status autentikasinya. Setelah itu, Django menyimpan informasi sesi di backend server (pada database) dan menyimpan kunci sesi dalam cookie di browser pengguna.
- Cookie ini disebut sebagai session cookie dan memiliki id sesi yang unik. Django menggunakan id sesi yang ada dalam cookie untuk mencari data sesi yang sesuai di server.

**Kegunaan lain dari cookies**
- Pelacakan pengguna. Cookies digunakan untuk melacak aktivitas pengguna pada situs web.
- Preferensi pengguna. Cookies dapat menyimpan preferensi pengguna, seperti bahasa pilihan, tema tampilan, atau setelan lainnya sehingga situs web dapat memberikan pengalaman yang lebih personal.
- Penyimpanan Sementara. Cookies digunakan untuk menyimpan data sementara yang diperlukan antara beberapa halaman dalam sesi pengguna.

Namun, **tidak semua cookies aman untuk digunakan**. Terdapat beberapa risiko dan pertimbangan keamanan yang perlu diperhatikan, yaitu:
- Cookies rentan terhadap serangan Cross-Site Scripting (XSS). Jika cookies tidak diamankan dengan benar, data dapat dicuri oleh peretas melalui serangan XSS.
-  Cookies dapat digunakan untuk mengirim permintaan berbahaya atas nama pengguna yang sah, serangan ini disebut Cross-Site Request Forgery (CSRF)
- Cookies pihak ketiga (Third-party Cookies) sering digunakan untuk pelacakan lintas situs dan periklanan. Cookies ini sering dianggap invasif terhadap privasi dan sering diblokir oleh browser modern.

**5. Step-by-step implementasi checklist**
- pertama-tama, saya menambah import ```UserCreationForm```, ```AuthenticationForm```, ```authenticate```, ```login```, ```logout```, ```login_required```, ```HttpResponseRedirect```, ```datetime```, ```reverse```, dan ```messages``` pada file ```views.py``` saya. bagian import pada file ```views.py``` saya menjadi seperti ini.

```bash
from django.shortcuts import render, redirect
from main.forms import GetSupplyForm
from main.models import Product
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
import datetime
...
```
- import ```login```, ```logout```, dan ```login_required``` berfungsi untuk memanggil fungsi bawaan Django untuk melakukan login, logout, dan merestriksi akses halaman main.
- import ```UserCreationForm```, ```AuthemticationForm```, dan ```authenticate``` berfungsi untuk memanggil fungsi bawaan Django untuk melakukan autentikasi dan membuat formulir pendaftaran pengguna pada aplikasi web.
- import ```datetime``` berfungsi untuk mendapatkan waktu saat ini ketika mengakses web.
- import ```reverse``` berfungsi untuk mendapatkan fungsi bawaan Django yang digunakan untuk mendapatkan URL dari nama pola URL yang didefinisikan pada file ```urls.py```. import ```HttpResponseRedirect``` adalah fungsi yang digunakan untuk melakukan redirect pengguna ke URL tertentu.
- lalu saya membuat fungsi ```register``` pada file ```views.py``` saya untuk menghasilkan formulir secara otomatis dan menghasilkan akun pengguna ketika data di-submit dari form.

```bash
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
```

- setelah itu, saya membuat tampilan untuk page register saya dengan membuat file html baru yang saya namakan ```register.html```, berikut isi dari file tersebut.

```bash
{% extends 'base.html' %}

{% block meta %}
<title>Register</title>
{% endblock meta %}

{% block content %}

<div class="login">
  <h1>Register</h1>

  <form method="POST">
    {% csrf_token %}
    <table>
      {{ form.as_table }}
      <tr>
        <td></td>
        <td><input type="submit" name="submit" value="Daftar" /></td>
      </tr>
    </table>
  </form>

  {% if messages %}
  <ul>
    {% for message in messages %}
    <li>{{ message }}</li>
    {% endfor %}
  </ul>
  {% endif %}
</div>

{% endblock content %}
```

- lalu, saya membuat fungsi ```login_user``` dan ```logout_user``` yang berfungsi untuk menangani login dan logout user pada aplikasi web saya serta menambahkan ```@login_required(login_url='/login')``` untuk merestriksi agar halaman main hanya dapat diakses oleh pengguna yang sudah login. berikut bentuk modifikasi dan fungsinya.

```bash
...
@login_required(login_url='/login')
def show_products(request):
...

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
        form = AuthenticationForm(request)
    context = {'form': form}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response
```

- lalu saya menambahkan potongan kode ```'last_login': request.COOKIES['last_login'],``` pada ```show_products``` saya di file ```views.py```

```bash
...
'product_entries' : product_entries,
        'last_login' : request.COOKIES['last_login'],
    }
...
```

- lalu, saya melakukan beberapa modifikasi dan tambahan pada file ```urls.py``` saya dengan menambah path register, login, dan logout pada ```urlpatterns```. berikut bentuk kodenya.

```bash
from main.views import show_products, create_supply, show_json, show_json_by_id, show_xml, show_xml_by_id, register, login_user, logout_user
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
]
```

- setelah itu, saya membuat berkas ```login.html```. berikut isi dari berkas tersebut.

```bash
{% extends 'base.html' %}

{% block meta %}
<title>Login</title>
{% endblock meta %}

{% block content %}
<div class="login">
  <h1>Login</h1>

  <form method="POST" action="">
    {% csrf_token %}
    <table>
      {{ form.as_table }}
      <tr>
        <td></td>
        <td><input class="btn login_btn" type="submit" value="Login" /></td>
      </tr>
    </table>
  </form>

  {% if messages %}
  <ul>
    {% for message in messages %}
    <li>{{ message }}</li>
    {% endfor %}
  </ul>
  {% endif %} Don't have an account yet?
  <a href="{% url 'main:register' %}">Register Now</a>
</div>

{% endblock content %}
```

- lalu, saya melakukan modifikasi pada file ```main.html``` saya dengan menambahkan tombol logout dan menampilkan sesi terakhir login user. berikut penambahannya.

```bash
...
<a href="{% url 'main:logout' %}">
  <button>Logout</button>
</a>

<h5> Sesi terakhir login: {{ last_login }}</h5>
{% endblock content %}
```

- setelah itu, saya melakukan beberapa modifikasi pada ```models.py``` saya. berikut modifikasinya.

```bash
...
from django.contrib.auth.models import User

class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
...
```

- lalu, saya kembali membuka ```views.py``` dan melakukan beberapa modifikasi pada fungsi ```create_supply``` saya agar objek yang diinput hanya dimiliki oleh pengguna yang sedang login dan melakukan input tersebut. berikut perubahannya.

```bash
...
def create_supply(request):
    form = GetSupplyForm(request.POST, request.FILES or None)
    if form.is_valid() and request.method == 'POST':
        supply_entry = form.save(commit=False)
        supply_entry.user = request.user
        supply_entry.save()
        return redirect('main:show_products')
    
    context = {"form": form}
    return render(request, 'create_supply.html', context)
...
```

- lalu, saya mengubah value dari ```product_entries``` dan ```content``` pada fungsi ```show_products``` saya menjadi berikut.

```bash
...
def show_products(request):
    product_entries = Product.objects.filter(user=request.user)
    content = {
        'user_name': request.user.username,
        'name' : 'Ultra Milk 1 L Full Cream',
        'price' : 20000,
        'description' : 'Ultra milk 1L full cream with plain flavor',
        'image' : 'https://i.imgur.com/Xe74ORV.jpeg',
        'product_entries' : product_entries,
        'last_login' : request.COOKIES['last_login'],
    }
    
    return render(request, 'main.html', content)
...
```
- lalu saya membuat sebuah akun pada local dan melakukan migrasi
- lalu, saya melakukan modifikasi dan menambahkan import ```os``` pada ```settings.py``` saya. berikut perubahannya.

```bash
...
from pathlib import Path
import os
...
PRODUCTION = os.getenv("PRODUCTION", False)
DEBUG = not PRODUCTION
...
```

- lalu, saya membuat satu akun pengguna lain dengan masing tiga dummy data.

**Akun dengan username rafif.sulaiman**

![Screenshot (35)](https://github.com/user-attachments/assets/07c8f2f6-2df7-4658-a3e7-94e9544d958c)

**Akun dengan username sulaiman.rafif**

![Screenshot (36)](https://github.com/user-attachments/assets/14c8c742-f506-4bef-a7af-ebe77036e171)

# TUGAS 5
[Back to Table of Contents](#table-of-contents)
## Jawaban
**1. Prioritas CSS selector**
Urutan prioritas yang akan diterapkan ketika ada beberapa selector dengan elemen yang sama adalah, !important, Inline Styles, ID Selector, Class (Class, Pseudo-class, dan Attribute Selector), Tag Selector, terakhir Universal Selector dan Inheritance. Jadi, ketika terdapat selector-selector seperti ini

```bash
p {
  color: black;
}

p.example {
  color: green;
}

#example {
  color: blue;
}

p[title="example"] {
  color: purple;
}

p {
  color: red !important;
}
```

Yang akan diutamakan adalah ```color: red !important;``` karena terdapat !important.

**2. Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web?**
Responsive design menjadi sangat penting karena:
  - Pengguna bisa mendapatkan pengalaman yang optimal pada berbagai ukuran layar tanpa harus melakukan zoom yang berlebihan.
  - Dengan menggunakan responsive design, aplikasi web dapat diakses oleh berbagai pengguna walaupun ukuran layarnya beragam.
  - Responsive design membuat para developer tidak perlua membuat situs untuk masing-masing ukuran layar pengguna, cukup satu situs yang dapat bekerja di semua perangkat.

Aplikasi-aplikasi yang sudah menerapkan responsive design:
  - YouTube
  - Twitter

Aplikasi-aplikasi yang belum menerapkan responsive design:
  - Instagram
  - Craigslist

**3. Perbedaan Margin, Border, dan Padding**
- *Margin* adalah ruang di luar elemen, yang berarti margin menentukan jarak antara elemen satu dengan elemen lainnya. Contoh penggunaan:

```bash
div {
  margin: 20px; /* Menambahkan margin 20px pada semua sisi */
  margin-top: 10px; /* Menambahkan margin 10px di bagian atas */
  margin-right: 15px; /* Menambahkan margin 15px di sisi kanan */
  margin-bottom: 5px; /* Menambahkan margin 5px di bagian bawah */
  margin-left: 25px; /* Menambahkan margin 25px di sisi kiri */
}
```

- *Border* adalah garis yang mengelilingi padding di konten elemen, berguna untuk membuat suatu batas visual di sekitar elemen. Contoh penggunaan:

```bash
div {
  border: 2px solid blue; /* Border biru dengan ketebalan 2px */
  border-width: 5px; /* Mengatur ketebalan border */
  border-style: dashed; /* Mengatur border menjadi garis putus-putus */
  border-color: red; /* Warna border merah */
}
```

- *Padding* adalah ruang di dalam elemen, yang berarti padding berguna untuk mengatur jarak di dalam elemen, antara konten dan border. Contoh penggunaan:

```bash
div {
  padding: 10px; /* Menambahkan padding 10px di semua sisi */
  padding-top: 15px; /* Padding 15px di bagian atas */
  padding-right: 20px; /* Padding 20px di sisi kanan */
  padding-bottom: 5px; /* Padding 5px di bagian bawah */
  padding-left: 30px; /* Padding 30px di sisi kiri */
}
```

**4. Konsep *flex box* dan *grid layout* serta kegunaannya**
  - *Flex box* adalah model yang berfungsi untuk menentukan tata letak elemen pada satu dimensi, antara baris atau kolom. *Flex box* digunakan untuk mendistribusikan ruang di antara item dalam sebuah container. Kegunaan flex box:
    - Flex box memungkinkan elemen-elemen dalam container untuk berubah ukuran secara otomatis sesuai dengan ruang yang tersedia
    - Flex box menyediakan kontrol penuh atas distribusi ruang, penataan spasi antar-elemen, dan perataan item
    - Flex box mempermudah pembuatan responsive design
  
  - *Grid layout* adalah model yang berfungsi untuk menentukan tata letak elemen pada dua dimensi, memungkinkan developer untuk menata elemen-elemen dalam baris dan kolom sekaligus. *Grid layout* cocok digunakan untuk membuat layout kompleks di mana elemen-elemen ditempatkan pada grid yang diatur dalam beberapa baris dan kolom. Kegunaan grid layout:
    - Grid layout memungkinkan pengaturan tata letak baris dan kolom, sehingga memudahkan developer ketika membuat struktur halaman yang kompleks
    - Grid layout memungkinkan tata letak yang fleksibel dan responsif (dapat berubah-ubah mengikuti ukuran layar)
    - Dengan grid layout, elemen dapat dengan mudah diatur agar mengisi area grid tertentu tanpa harus menulis kode yang rumit

**5. Step-by-step Implementasi Checklist**
- pertama-tama, saya menambahkan Tailwind ke proyek Django saya dengan menambahkan baris kode ini pada ```base.html``` saya.

```bash
<head>
{% block meta %}
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1">
{% endblock meta %}
<script src="https://cdn.tailwindcss.com">
</script>
</head>
```

- lalu saya menambahkan fungsi baru pada ```views.py``` saya, yaitu ```edit_product``` dan ```delete_product```.

```bash
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
```

- selain itu saya juga menambahkan import ```reverse``` dan ```HttpResponseRedirect``` pada file ```views.py``` saya.
- lalu, saya membuat file html untuk page edit_product saya pada subdirektori ```main/templates```. berikut isi ```edit_product.html```.

```bash
{% extends 'base.html' %}
{% load static %}
{% block meta %}
<title>Edit Product</title>
{% endblock meta %}

{% block content %}
{% include 'navbar.html' %}
<div class="flex flex-col min-h-screen bg-gray-100 dark:bg-gray-900 transition-colors duration-500">
  <div class="container mx-auto px-4 py-8 mt-16 max-w-xl">
    <h1 class="text-3xl font-bold text-center mb-8 text-black dark:text-white">Edit Product</h1>
  
    <div class="bg-white dark:bg-gray-800 rounded-lg p-6 form-style">
      <form method="POST" class="space-y-6">
          {% csrf_token %}
          {% for field in form %}
              <div class="flex flex-col">
                  <label for="{{ field.id_for_label }}" class="mb-2 font-semibold text-gray-700 dark:text-gray-300">
                      {{ field.label }}
                  </label>
                  <div class="w-full">
                      {{ field }}
                  </div>
                  {% if field.help_text %}
                      <p class="mt-1 text-sm text-gray-500 dark:text-gray-400">{{ field.help_text }}</p>
                  {% endif %}
                  {% for error in field.errors %}
                      <p class="mt-1 text-sm text-red-600">{{ error }}</p>
                  {% endfor %}
              </div>
          {% endfor %}
          <div class="flex justify-center mt-6">
              <button type="submit" class="bg-indigo-600 dark:bg-indigo-500 text-white font-semibold px-6 py-3 rounded-lg hover:bg-indigo-700 dark:hover:bg-indigo-600 transition duration-300 ease-in-out w-full">
                  Edit Product
              </button>
          </div>
      </form>
    </div>
  </div>
</div>
{% endblock %}
```

- dan menambahkan tombol untuk delete dan edit product saya pada ```main.html```. berikut tambahan kode nya

```bash
<td>
        <a href="{% url 'main:edit_product' product_entry.pk %}">
            <button>
                Edit
            </button>
        </a>
    </td>
    <td>
        <a href="{% url 'main:delete_product' product_entry.pk %}">
            <button>
                Delete
            </button>
        </a>
    </td>
```

- lalu, saya membuka ```urls.py``` saya pada folder ```main``` untuk melakukan import fungsi edit dan delete, serta membuat path untuk masing-masing fungsi.

```bash
from main.views import show_products, create_supply, show_json, show_json_by_id, show_xml, show_xml_by_id, register, login_user, logout_user, edit_product, delete_product
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
]
```

- lalu saya membuat navigation bar pada proyek saya melalui file ```navbar.html``` yang saya letakkan pada folder templates di root directory proyek saya. berikut isi dari filenya.

```bash
<nav class="bg-black shadow-lg fixed top-0 left-0 z-40 w-screen dark:bg-gray-800">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 flex items-center justify-between h-16">
    <!-- Logo mentok ke kiri -->
    <div class="absolute left-7 pr-4">
      <h1 class="text-2xl font-bold text-purple-400 dark:text-purple-300">GetSupply</h1>
    </div>

    <div class="hidden md:flex items-center justify-center h-16 space-x-4 mx-auto">
      {% if user.is_authenticated %}
        <!-- Links -->
        <a href="{% url 'main:show_products' %}" class="hover:bg-purple-600 text-white font-bold py-2 px-4 rounded-lg transition duration-300">
          Home
        </a>

        <a href="{% url 'main:create_supply' %}" class="hover:bg-purple-600 text-white font-bold py-2 px-4 rounded-lg transition duration-300">
          Add New Product
        </a>

        <a href="{% url 'main:show_products' %}#products" class="hover:bg-purple-600 text-white font-bold py-2 px-4 rounded-lg transition duration-300">
          View Products
        </a>

        <!-- Theme Toggle Button (Desktop) -->
        <button id="theme-toggle-desktop" class="bg-gray-200 dark:bg-gray-600 dark:text-white text-black font-bold py-2 px-4 rounded-lg transition duration-300">
          Switch to Night Mode
        </button>

        <!-- Logout Button -->
        <a href="{% url 'main:logout' %}" class="bg-red-500 hover:bg-red-600 text-white font-bold py-2 px-4 rounded-lg transition duration-300">
          Logout
        </a>
      {% endif %}
    </div>

    <div class="hidden md:flex absolute right-0 pr-4">
      <span class="text-purple-300 mr-4 dark:text-purple-200">Welcome, {{ user.username }}</span>
    </div>

    <!-- Mobile menu button -->
    <div class="md:hidden flex items-center ml-auto">
      <button class="mobile-menu-button">
        <svg class="w-6 h-6 text-white" fill="none" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" stroke="currentColor">
          <path d="M4 6h16M4 12h16M4 18h16"></path>
        </svg>
      </button>
    </div>
  </div>

  <!-- Mobile menu -->
  <div class="mobile-menu hidden md:hidden px-4 w-full md:max-w-full">
    <div class="pt-2 pb-3 space-y-1 mx-auto">
      {% if user.is_authenticated %}
        <!-- Welcome message buat mobile view -->
        <span class="block text-gray-300 dark:text-gray-200">Welcome, {{ user.username }}</span>

        <!-- Mobile Links -->
        <a href="{% url 'main:show_products' %}" class="block hover:bg-purple-600 text-white font-bold py-2 px-4 rounded-lg transition duration-300">
          Home
        </a>

        <a href="{% url 'main:create_supply' %}" class="block hover:bg-purple-600 text-white font-bold py-2 px-4 rounded-lg transition duration-300">
          Add New Product
        </a>

        <a href="{% url 'main:show_products' %}#products" class="block hover:bg-purple-600 text-white font-bold py-2 px-4 rounded-lg transition duration-300">
          View Products
        </a>

        <!-- Theme Toggle Button (Mobile) -->
        <button id="theme-toggle-mobile" class="bg-gray-200 dark:bg-gray-600 dark:text-white text-black font-bold py-2 px-4 rounded-lg transition duration-300">
          Switch to Night Mode
        </button>

        <!-- Logout Button -->
        <a href="{% url 'main:logout' %}" class="block text-center bg-red-500 hover:bg-red-600 text-white font-bold py-2 px-4 rounded-lg transition duration-300">
          Logout
        </a>
      {% else %}
        <a href="{% url 'main:login' %}" class="block text-center bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-4 rounded-lg transition duration-300">
          Login
        </a>
        <a href="{% url 'main:register' %}" class="block text-center bg-green-500 hover:bg-green-600 text-white font-bold py-2 px-4 rounded-lg transition duration-300">
          Register
        </a>
      {% endif %}
    </div>
  </div>

  <!-- Script buat mobile menu dan tombol tema -->
  <script>
    const mobileMenuButton = document.querySelector('.mobile-menu-button');
    const mobileMenu = document.querySelector('.mobile-menu');

    mobileMenuButton.addEventListener('click', () => {
      mobileMenu.classList.toggle('hidden');
    });

    //tombol tema
    const themeToggleDesktop = document.getElementById('theme-toggle-desktop');
    const themeToggleMobile = document.getElementById('theme-toggle-mobile');
    const currentTheme = localStorage.getItem('theme') || 'light';

    //if dan else sesuai dengan tema yang dipilih
    if (currentTheme === 'dark') {
      document.documentElement.classList.add('dark');
      themeToggleDesktop.textContent = 'Switch to Day Mode';
      themeToggleMobile.textContent = 'Switch to Day Mode';
    } else {
      document.documentElement.classList.add('light');
      themeToggleDesktop.textContent = 'Switch to Night Mode';
      themeToggleMobile.textContent = 'Switch to Night Mode';
    }

    //fungsi buat milih tema
    function toggleTheme() {
      if (document.documentElement.classList.contains('dark')) {
        document.documentElement.classList.remove('dark');
        document.documentElement.classList.add('light');
        localStorage.setItem('theme', 'light');
        themeToggleDesktop.textContent = 'Switch to Night Mode';
        themeToggleMobile.textContent = 'Switch to Night Mode';
      } else {
        document.documentElement.classList.remove('light');
        document.documentElement.classList.add('dark');
        localStorage.setItem('theme', 'dark');
        themeToggleDesktop.textContent = 'Switch to Day Mode';
        themeToggleMobile.textContent = 'Switch to Day Mode';
      }
    }

    themeToggleDesktop.addEventListener('click', toggleTheme);
    themeToggleMobile.addEventListener('click', toggleTheme);
  </script>
</nav>
```

- lalu saya melakukan konfigurasi untuk static files pada aplikasi saya dengan menambahkan beberapa baris kode pada ```settings.py``` saya.

```bash
...
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', #Tambahkan tepat di bawah SecurityMiddleware
    ...
]
...
STATIC_URL = '/static/'
if DEBUG:
    STATICFILES_DIRS = [
        BASE_DIR / 'static' # merujuk ke /static root project pada mode development
    ]
else:
    STATIC_ROOT = BASE_DIR / 'static' # merujuk ke /static root project pada mode production
...
```

- lalu, untuk melakukan styling melalui css dan tailwind, saya membuat file ```global.css``` di ```/static/css``` pada root directory. berikut isi dari file ```global.css``` saya

```bash
.form-style form input, form textarea, form select {
    width: 100%;
    padding: 0.5rem;
    border: 2px solid #bcbcbc;
    border-radius: 0.375rem;
}
.form-style form input:focus, form textarea:focus, form select:focus {
    outline: none;
    border-color: #674ea7;
    box-shadow: 0 0 0 3px #674ea7;
}
@keyframes shine {
    0% { background-position: -200% 0; }
    100% { background-position: 200% 0; }
}
.animate-shine {
    background: linear-gradient(120deg, rgba(255, 255, 255, 0.3), rgba(255, 255, 255, 0.1) 50%, rgba(255, 255, 255, 0.3));
    background-size: 200% 100%;
    animation: shine 3s infinite;
}
```

- lalu saya melakukan styling untuk masing-masing file html saya. berikut isi dari ```base.html``` saya yang sudah saya modifikasi.

```bash
{% load static %}
<!DOCTYPE html>
<html lang="en" class="light">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    {% block meta %} {% endblock meta %}
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="{% static 'css/global.css' %}"/>
    <script>
      tailwind.config = {
        darkMode: 'class', // Aktifkan dark mode berbasis class
        theme: {
          extend: {},
        }
      }
    </script>
  </head>

  <body class="bg-gray-100 dark:bg-gray-900 dark:text-gray-100 transition-colors duration-500">
    {% block content %} {% endblock content %}
    
    <!-- Theme Toggle Script -->
    <script>
        document.addEventListener("DOMContentLoaded", function () {
          // Ambil tombol switch tema
          const themeToggle = document.getElementById('theme-toggle');
          const currentTheme = localStorage.getItem('theme') || 'light';
      
          // Terapkan tema saat ini pada elemen <html>
          if (currentTheme === 'dark') {
            document.documentElement.classList.add('dark');
            if (themeToggle) themeToggle.textContent = 'Switch to Day Mode';
          } else {
            document.documentElement.classList.add('light');
            if (themeToggle) themeToggle.textContent = 'Switch to Night Mode';
          }
      
          // Mengubah tema ketika tombol diklik
          if (themeToggle) {
            themeToggle.addEventListener('click', function () {
              if (document.documentElement.classList.contains('dark')) {
                document.documentElement.classList.remove('dark');
                document.documentElement.classList.add('light');
                localStorage.setItem('theme', 'light');
                themeToggle.textContent = 'Switch to Night Mode';
              } else {
                document.documentElement.classList.remove('light');
                document.documentElement.classList.add('dark');
                localStorage.setItem('theme', 'dark');
                themeToggle.textContent = 'Switch to Day Mode';
              }
            });
          }
        });
    </script>
  </body>
</html>
```

- modifikasi pada ```main.html``` saya

```bash
{% extends 'base.html' %}
{% load static %}

{% block meta %}
<title>GetSupply</title>
{% endblock meta %}
{% block content %}
{% include 'navbar.html' %}
<div class="overflow-x-hidden px-4 md:px-8 pb-8 pt-24 min-h-screen bg-gray-100 dark:bg-gray-900 flex flex-col transition-colors duration-500">
  <div class="p-2 mb-6 relative">
    <p class="text-center text-gray-600 dark:text-gray-100 font-bold text-3xl mb-8">Welcome to GetSupply!</p>
    <div class="relative grid grid-cols-1 z-30 md:grid-cols-3 gap-8">
      {% include "card_info.html" with title='Name' value=name %}
      {% include "card_info.html" with title='NPM' value=npm %}
      {% include "card_info.html" with title='Class' value=class %}
    </div>
  </div>

  <!-- Bar bertuliskan "Products" -->
  <div class="w-full bg-purple-700 dark:bg-purple-800 text-center dark:bg-purple-500 text-white dark:text-gray-200 text-2xl font-bold p-3 rounded-md mb-4">
    Products
  </div>
  
  <!-- Kondisi Produk -->
  <section id="products" class="bg-gray-100 dark:bg-gray-900 dark:text-gray-100 transition-colors duration-500">
    {% if not product_entries %}
    <div class="flex flex-col items-center justify-center min-h-[24rem] p-6">
      <img src="{% static 'gif/laughing.gif' %}" alt="Sad face" class="w-45 h-45 mb-4"/>
      <p class="text-center text-gray-600 dark:text-gray-400 font-bold text-xl mt-4">Belum ada data product pada GetSupply.</p>
    </div>
    {% else %}
    <div class="columns-1 sm:columns-2 lg:columns-3 gap-6 space-y-6 w-full">
      {% for product_entry in product_entries %}
      {% include 'card_product.html' with product_entry=product_entry %}
      {% endfor %}
    </div>
    {% endif %}
  </section>
  
  <!-- Last Login -->
  <div class="px-0 mt-6">
    <div class="flex rounded-md items-center bg-purple-600 dark:bg-purple-500 py-2 px-4 w-fit">
      <h1 class="text-white text-center dark:text-gray-200">Last Login: {{last_login}}</h1>
    </div>
  </div>
</div>
{% endblock content %}
```

- modifikasi pada ```register.html``` saya

```bash
{% extends 'base.html' %}
{% include 'navbar.html' %}

{% block meta %}
<title>Register</title>
{% endblock meta %}

{% block content %}
<div class="min-h-screen flex items-center justify-center bg-gray-100 py-12 px-4 sm:px-6 lg:px-8">
  <div class="container-box">
    <div class="text-center">
      <h1 class="getsupply-logo text-center text-4xl mb-10 font-bold text-gray-900">GetSupply</h1>
      <p class="mb-4 text-gray-600">Sign up to access our services and store your products.</p>

    <form class="space-y-4" method="POST">
      {% csrf_token %}
      <input type="hidden" name="remember" value="true">
      <div class="rounded-md shadow-sm space-y-4">
        {% for field in form %}
          <div>
            <input id="{{ field.id_for_label }}" name="{{ field.name }}" type="{{ field.field.widget.input_type }}" placeholder="{{ field.label }}" required class="appearance-none rounded w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm">
            {% if field.errors %}
              {% for error in field.errors %}
                <p class="mt-1 text-sm text-red-600">{{ error }}</p>
              {% endfor %}
            {% endif %}
          </div>
        {% endfor %}
      </div>

      <div class="mt-4">
        <button type="submit" class="w-full bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-4 rounded">
          Sign up
        </button>
      </div>
    </form>

    {% if messages %}
    <div class="mt-4">
      {% for message in messages %}
      <div class="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded relative" role="alert">
        <span class="block sm:inline">{{ message }}</span>
      </div>
      {% endfor %}
    </div>
    {% endif %}

    <div class="text-center mt-4">
      <p class="text-sm text-gray-500">
        Already have an account?
        <a href="{% url 'main:login' %}" class="font-medium text-blue-500 hover:underline">
          Login here
        </a>
      </p>
    </div>
  </div>
</div>

<style>
  .container-box {
    max-width: 700px; /* Adjust the max-width to make the container bigger */
    width: 100%; /* Ensure it takes up the full width up to max-width */
    padding: 50px; /* Increase padding for a larger container */
    background-color: white; /* White background for the box */
    border-radius: 10px; /* Slight rounding for smooth corners */
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* Soft shadow for better visibility */
  }
  
  .getsupply-logo {
    {% comment %} font-family: 'Comic Sans MS', cursive; {% endcomment %}
    font-size: 50px;
  }

  .form-style input {
    background-color: #fafafa;
    border-color: #dbdbdb;
  }

  .form-style input:focus {
    border-color: #a8a8a8;
  }

  .bg-blue-500 {
    background-color: #0095f6;
  }

  .bg-blue-500:hover {
    background-color: #007ac6;
  }

  .text-gray-500 {
    color: #8e8e8e;
  }

  input {
    width: 100%;
    padding: 20px; /* Larger padding for bigger field */
    font-size: 18px; /* Larger font size */
    border: 1px solid #dbdbdb;
    border-radius: 5px;
    box-sizing: border-box;
  }

  button {
    width: 100%;
    padding: 20px; /* Larger button */
    font-size: 18px;
    background-color: #0095f6;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
  }

  button:hover {
    background-color: #007ac6;
  }
</style>
{% endblock content %}
```

- modifikasi pada ```login.html``` saya

```bash
{% extends 'base.html' %}
{% include 'navbar.html' %}

{% block meta %}
<title>Login</title>
{% endblock meta %}

{% block content %}
<div class="login-container flex items-center justify-center h-screen bg-gray-700">
  <div class="login-box bg-white p-10 rounded-lg shadow-md max-w-md w-full">
    <h1 class="getsupply-logo text-center text-4xl mb-10 font-bold text-gray-900">GetSupply</h1>
    <h2 class="login-info text-left text-1l mb-1 font-bold text-red-600">Log In To Your Account</h2>
    
    <form class="space-y-6" method="POST" action="">
      {% csrf_token %}
      <div class="rounded-md shadow-sm">
        <div>
          <input id="username" name="username" type="text" required 
                 class="appearance-none rounded-t-md w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm" 
                 placeholder="Username">
        </div>
        <div>
          <input id="password" name="password" type="password" required 
                 class="appearance-none rounded-b-md w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm" 
                 placeholder="Password">
        </div>
      </div>

      <div>
        <button type="submit" 
                class="w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-blue-500 hover:bg-blue-600 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500">
          Log In
        </button>
      </div>
    </form>

    {% if messages %}
    <div class="mt-4">
      {% for message in messages %}
      {% if message.tags == "success" %}
            <div class="bg-green-100 border border-green-400 text-green-700 px-4 py-3 rounded relative" role="alert">
                <span class="block sm:inline">{{ message }}</span>
            </div>
        {% elif message.tags == "error" %}
            <div class="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded relative" role="alert">
                <span class="block sm:inline">{{ message }}</span>
            </div>
        {% else %}
            <div class="bg-blue-100 border border-blue-400 text-blue-700 px-4 py-3 rounded relative" role="alert">
                <span class="block sm:inline">{{ message }}</span>
            </div>
        {% endif %}
      {% endfor %}
    </div>
    {% endif %}

    <div class="text-center mt-4">
      <p class="text-sm text-gray-500">
        Don't have an account?
        <a href="{% url 'main:register' %}" class="font-medium text-blue-500 hover:underline">
          Sign up
        </a>
      </p>
    </div>
  </div>
</div>

<style>
  .login-container {
      background-color: #fafafa;
      padding: 40px;
  }

  .login-box {
    border: 1px solid #dbdbdb;
    padding: 50px; /* Adjust padding if necessary */
    max-width: 700px; /* Increase this value to make it wider */
    width: 100%; /* Make it responsive */
    margin-top: 0;
  }

  .login-info {
    font-size: 15px;
  }

  .getsupply-logo {
      {% comment %} font-family: 'Comic Sans MS', cursive; {% endcomment %}
      font-size: 50px;
  }

  .rounded-md input {
      background-color: #fafafa;
      border-color: #dbdbdb;
  }

  .rounded-md input:focus {
      border-color: #a8a8a8;
  }

  .bg-blue-500 {
      background-color: #0095f6;
  }

  .bg-blue-500:hover {
      background-color: #007ac6;
  }

  .text-gray-500 {
      color: #8e8e8e;
  }

  h2 {
    margin-bottom: 10px;
  }
</style>

{% endblock content %}
```

- modifikasi pada ```create_supply.html``` saya

```bash
{% extends 'base.html' %}
{% load static %}
{% load widget_tweaks %}
{% block meta %}
<title>Create Product</title>
{% endblock meta %}

{% block content %}
{% include 'navbar.html' %}

<div class="flex flex-col min-h-screen bg-gray-100 dark:bg-gray-900 transition-colors duration-500">
  <div class="container mx-auto px-4 py-8 mt-16 max-w-xl">
    <h1 class="text-3xl font-bold text-center mb-8 text-black dark:text-white">Create New Product</h1>
  
    <div class="bg-white dark:bg-gray-800 shadow-md rounded-lg p-6 form-style">
      <form method="POST" enctype="multipart/form-data" class="space-y-6">
        {% csrf_token %}
        {% for field in form %}
          <div class="flex flex-col">
            <label for="{{ field.id_for_label }}" class="mb-2 font-semibold text-gray-700 text-lg dark:text-gray-300">
              {{ field.label }}
            </label>
            <div class="w-full">
              {{ field|add_class:"text-black dark:text-white dark:bg-gray-600" }}
            </div>
            {% if field.help_text %}
              <p class="mt-1 text-sm text-gray-500 dark:text-gray-400">{{ field.help_text }}</p>
            {% endif %}
            {% for error in field.errors %}
              <p class="mt-1 text-sm text-red-600">{{ error }}</p>
            {% endfor %}
          </div>
        {% endfor %}
        <div class="flex justify-center mt-6">
          <button type="submit" class="bg-purple-600 dark:bg-purple-500 text-white font-semibold px-6 py-3 rounded-lg hover:bg-purple-700 dark:hover:bg-purple-600 transition duration-300 ease-in-out w-full">
            Create New Product
          </button>
        </div>
      </form>
    </div>
  </div>
</div>

{% endblock %}
```

- modifikasi pada ```edit_product.html``` saya

```bash
{% extends 'base.html' %}
{% load static %}
{% block meta %}
<title>Edit Product</title>
{% endblock meta %}

{% block content %}
{% include 'navbar.html' %}
<div class="flex flex-col min-h-screen bg-gray-100 dark:bg-gray-900 transition-colors duration-500">
  <div class="container mx-auto px-4 py-8 mt-16 max-w-xl">
    <h1 class="text-3xl font-bold text-center mb-8 text-black dark:text-white">Edit Product</h1>
  
    <div class="bg-white dark:bg-gray-800 rounded-lg p-6 form-style">
      <form method="POST" class="space-y-6">
          {% csrf_token %}
          {% for field in form %}
              <div class="flex flex-col">
                  <label for="{{ field.id_for_label }}" class="mb-2 font-semibold text-gray-700 dark:text-gray-300">
                      {{ field.label }}
                  </label>
                  <div class="w-full">
                      {{ field }}
                  </div>
                  {% if field.help_text %}
                      <p class="mt-1 text-sm text-gray-500 dark:text-gray-400">{{ field.help_text }}</p>
                  {% endif %}
                  {% for error in field.errors %}
                      <p class="mt-1 text-sm text-red-600">{{ error }}</p>
                  {% endfor %}
              </div>
          {% endfor %}
          <div class="flex justify-center mt-6">
              <button type="submit" class="bg-indigo-600 dark:bg-indigo-500 text-white font-semibold px-6 py-3 rounded-lg hover:bg-indigo-700 dark:hover:bg-indigo-600 transition duration-300 ease-in-out w-full">
                  Edit Product
              </button>
          </div>
      </form>
    </div>
  </div>
</div>
{% endblock %}
```

- lalu saya membuat masing-masing file ```card_info.html``` dan ```card_product.html```, berikut isi dari masing-masing filenya.
- ```card_product.html```

```bash
<div class="relative break-inside-avoid bg-purple-100 shadow-md rounded-lg mb-6 border-2 border-purple-300 dark:bg-gray-700 max-w-full">
    <!-- Flex container for image and content -->
    <div class="flex items-start p-4 space-x-4 min-w-0">
        <!-- Product image on the left -->
        <div class="flex-shrink-0">
            <img src="{{ product_entry.image.url }}" alt="Gambar Produk" width="300" height="400" class="rounded-xl">
        </div>

        <!-- Product content on the right -->
        <div class="w-0 flex-grow">
            <h3 class="font-bold text-4xl mb-2 whitespace-normal break-words">{{ product_entry.name }}</h3>
            <p class="text-gray-600 text-xl mb-8 dark:text-gray-200">{{ product_entry.description }}</p>
            <hr class="border-t-2 border-gray-400 my-4">

            <div class="mt-4">
                <p class="text-2xl font-bold mt-4 mb-2">Price</p>
                <p class="text-gray-600 text-lg dark:text-gray-200">Rp. {{ product_entry.price }}</p>
            </div>
        </div>
    </div>

    <!-- Edit and Delete buttons -->
    <div class="flex justify-end p-4 space-x-2">
        <a href="{% url 'main:edit_product' product_entry.pk %}" class="bg-purple-500 hover:bg-purple-700 text-white rounded-full p-2 transition duration-300 shadow-md">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
                <path d="M13.586 3.586a2 2 0 112.828 2.828l-.793.793-2.828-2.828.793-.793zM11.379 5.793L3 14.172V17h2.828l8.38-8.379-2.83-2.828z" />
            </svg>
        </a>
        <a href="{% url 'main:delete_product' product_entry.pk %}" class="bg-amber-600 hover:bg-amber-700 text-white rounded-full p-2 transition duration-300 shadow-md">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
                <path fill-rule="evenodd" d="M9 2a1 1 0 00-.894.553L7.382 4H4a1 1 0 000 2v10a2 2 0 002 2h8a2 2 0 002-2V6a1 1 0 100-2h-3.382l-.724-1.447A1 1 0 0011 2H9zM7 8a1 1 0 012 0v6a1 1 0 11-2 0V8zm5-1a1 1 0 00-1 1v6a1 1 0 102 0V8a1 1 0 00-1-1z" clip-rule="evenodd" />
            </svg>
        </a>
    </div>
</div>
```

- ```card_info.html```

```bash
<div class="bg-purple-700 dark:bg-purple-900 rounded-xl overflow-hidden border-2 border-purple-800">
    <div class="p-4 animate-shine">
      <h5 class="text-lg font-semibold text-white">{{ title }}</h5>
      <p class="text-white">{{ value }}</p>
    </div>
</div>
```