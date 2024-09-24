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

- ```HttpResponseRedirect()``` adalah kelas respons yang mengembalikan respons HTTP 302 ke URL yang ditentukan. Untuk menggunakannya, perlu diberikan URL lengkap atau relatif sebagai argumen, seperti ```return HttpResponseRedirect('/url/')```. Untuk ini, perlu membangun URL sendiri, dan itu bisa menjadi lebih rumit jika URL memerlukan pengaturan khusus atau penggunaan fungsi pembalik URL (reverse).

- ```redirect()``` adalah fungsi yang menyediakan cara yang lebih mudah dan fleksibel untuk melakukan pengalihan. Fungsi ini dapat menerima URL, model instance, atau bahkan nama tampilan sebagai argumen, contohnya ```return redirect('view_name', arg1='value')```. Fungsi ini juga mendukung penggunaan fungsi pembalik (```reverse()```) untuk membangun URL dari nama tampilan.

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
    mood = models.CharField(max_length=255)
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
- Melalui kode diatas, ```Product``` akan terhubung dengan ```User``` yang membuat entry tersebut. Penghubungan ini memungkinkan server untuk melacak product setiap pengguna dan mengelola data secara terpisah berdasarkan pengguna yang login.


**3. Perbedaan antara Authentication dan Authorization:**

- Authentication adalah suatu proses untuk memverifikasi identitas pengguna dan memastikan apakah pengguna adalah siapa yang mereka klaim, tujuannya adalah untuk menentukan siapa pengguna tersebut. Biasanya melibatkan pemeriksaan kredensial seperti username/password, token, dan metode autentikasi lainnya.

- Authorization adalah suatu proses untuk menentukan apa yang dapat dilakukan oleh pengguna yang sudah terautentikasi. Bertujuan untuk menentukan apa yang diizinkan dan tidak diizinkan bagi pengguna dan melibatkan pengaturan izin dan aturan akses untuk menentukan apa saja yang bisa dilakukan oleh pengguna tertentu.

**Proses yang terjadi saat pengguna login**
- Pengguna memasukkan data kredensial (usernam dan password).
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
- Django menggunakan cookies dan session untuk menghubungkan pengguna dengan status autentikasinya. Setelah itu, Django menyimpan informasi sesi di backend server (seperti database, cache, dsb) dan menyimpan kunci sesi dalam cookie di browser pengguna.
- Cookie ini disebut sebagai session cookie dan meemiliki id sesi yang unik. Django menggunakan id sesi yang ada dalam cookie untuk mencari data sesi yang sesuai di server, sehingga dapat mengenali pengguna yang telah login.

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

- lalu, saya membuat dua akun pengguna dengan masing tiga dummy data.

**Akun dengan username rafif.sulaiman**

![Screenshot (35)](https://github.com/user-attachments/assets/07c8f2f6-2df7-4658-a3e7-94e9544d958c)

**Akun dengan username sulaiman.rafif**

![Screenshot (36)](https://github.com/user-attachments/assets/14c8c742-f506-4bef-a7af-ebe77036e171)