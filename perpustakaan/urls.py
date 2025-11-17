from django.contrib import admin
from django.urls import path,include
from .views import dashboard, profil,kontak,alamat,sejarah,buku,tambah_buku

urlpatterns = [
   path('',dashboard,name='dashboard'),
   path('profil/',profil,name='profil'),
   path('kontak/',kontak,name='kontak'),
   path('alamat/',alamat,name='alamat'),
   path('sejarah/',sejarah,name='sejarah'),
   path('buku/',buku,name='buku'),
    path('tambah_buku/',tambah_buku,name='tambah_buku'),
]
