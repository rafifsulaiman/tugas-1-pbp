Link PWS: 

1. untuk membuat sebuah proyek Django baru, saya membuat direktori baru pada file explorer saya, lalu membuka command prompt dan memasukkan perintah -m venv env, lalu menuliskan perintah env\Scripts\activate. ketika env sudah aktif, saya membuat requirements.txt berisikan dependencies-dependencies yang diperlukan, lalu melakukan perintah pada command prompt berupa pip install -r requirements.txt, lalu melakukan deactivate.

lalu, kita membuat proyek django dengan menjalankan perintah django-admin startproject get_supply. perintah tersebut berfungsi untuk membuat folder berdasarkan nama proyek saya dan sudah berisi file-file bawaan proyek dari django. setelah itu, saya menjalankan perintah python manage.py startapp main pada command prompt direktori proyek saya. perintah tersebut berfungsi untuk membuat folder main berisikan template-template bawaan dari Django pada direktori proyek saya.

lalu, saya menambahkan main ke dalam INSTALLED_APPS pada file settings.py bawaan Django. main yang dimaksud adalah file main.html yang terbuat ketika saya memulai proyek Django pada direktori proyek saya.

lalu pada berkas models.py, saya menambahkan class Product berisikan atribut-atribut yang menggunakan fungsi bawaan dari class Model pada Django. atribut-atribut yang saya definisikan adalah name, price, dan description yang diwajibkan serta saya menambahkan atribut baru untuk mempercantik tampilan berisikan gambar yang saya namakan image. berikut bentuk class dan atribut yang saya buat.

from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=300)
    price = models.IntegerField()
    description = models.TextField(max_length=300)
    image = models.ImageField() #upload image

setelah saya membuat atribut pada models.py, saya membuat dictionary yang berisikan data yang akan saya masukkan kedalam template HTML. data yang diperlukan saya letakkan pada file views.py dan berisikan seperti berikut.

from django.shortcuts import render

# Create your views here.
def show_products(request):
    content = {
        'name' : 'Ultra Milk 1 L Full Cream',
        'price' : 20000,
        'description' : 'Ultra milk 1L full cream with plain flavor',
        'image' : 'https://i.imgur.com/Xe74ORV.jpeg'
    }

    return render(request, 'main.html', content)

return render(request, 'main.html', content) berfungsi untuk mengantar isi dari dictionary content ke template HTML yang sudah saya buat, berikut isi dari template HTML-nya.

<h1>Welcome to GetSupply by Rafif Sulaiman Dirvesa/2306222771</h1>

<h5>Name: </h5>
<p>{{ name }}</p>
<h5>Price: </h5>
<p>{{ price }}</p>
<h5>Description: </h5>
<p>{{ description }}</p>
<img src="{{ image }}">

untuk melakukan pemetakan fungsi yang telah dibuat pada views.py, saya membuat routing sebagai berikut.

from main.views import show_products
from django.urls import path

app_name = 'main'
urlpatterns = [
    path('', show_products, name='show_products'),
]

setelah saya selesai membuat proyek, saya membuat repo baru dengan visibilitas public pada akun github saya untuk melakukan upload ke dalam github. pertama-tama, saya melakukan perintah git init pada command prompt direktori proyek saya, membuat branch baru dengan perintah git checkout -b main, melakukan add, commit, dan push, diakhiri dengan menjalankan perintah git push -u origin main (nama branch).

untuk melakukan upload pada PWS, saya membuka halaman PWS pada https://pbp.cs.ui.ac.id dan melakukan login. lalu saya membuat proyek baru pada PWS dengan menekan tombol Create New Project dan menamai proyeknya dengan tugas-1-pbp. lalu saya membuka kembali file settings.py saya dan menambahkan URL deployment PWS saya pada ALLOWED_HOST dengan format <username-sso>-<nama proyek>.pbp.cs.ui.ac.id dan melakukan git add, commit, dan push ke Github. lalu saya mengikuti tahapan-tahapan berupa perintah command prompt yang terdapat pada Project Command pada halaman PWS proyek saya. terakhir saya melakukan perintah pada command prompt berupa git branch -M main untuk mengubah branch utama menjadi main.

2.
![messageImage_1725905119582](https://github.com/user-attachments/assets/5dc1c04a-a684-48a3-8a75-fb18979ed9d7)

ketika ada HTTP request yang dilakukan melalui browsing platform, alamat HTTP akan dicek apakah sesuai dengan url yang berada pada file urls.py. jika sesuai, maka permintaan akan dilanjutkan ke file views.py yang berisikan data untuk atribut-atribut yang terdapat pada models.py. setelah mendapatkan data dan juga atribut, data dan atribut itu akan disalurkan ke template yang sudah dibuat dengan file main.html. setelah data masuk ke dalam template, template akan memberikan respon ke browsing platform dengan menyajikan tampilan web sesuai dengan template yang sudah dibuat.

4. git dapat menyimpan riwayat perubahan pada kode pengguna dan kembali ke versi sebelumnya, memfasilitasi kolaborasi tim pada proyek yang dikerjakan bersama, dan memungkinkan pengguna untuk membuat dan mengelola berbagai versi proyek.

5. karena framework django sangat ramah untuk dipelajari pemula, menyediakan banyak fitur built-in, dan memiliki banyak paket tambahan dan alat yang dapat memperluas fungsionalitasnya.

6. Model pada Django disebut ORM (Object-Relational Mapping) karena Django memungkinkan pengguna untuk berinteraksi dengan basis data menggunakan kode Python. ORM ini menyediakan cara untuk mendefinisikan model basis data menggunakan kelas Python dan secara otomatis menghasilkan petnyataan SQL untuk berinteraksi dengan basisi data berdasarkan model tersebut.
