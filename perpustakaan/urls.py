from django.contrib import admin
from django.urls import path,include
from .views import dashboard, profil,kontak,alamat,sejarah,buku

urlpatterns = [
   path('dashboard/',dashboard,name='dashboard'),
   path('profil/',profil,name='profil'),
   path('kontak/',kontak,name='kontak'),
   path('alamat/',alamat,name='alamat'),
   path('sejarah/',sejarah,name='sejarah'),
   path('buku/',buku,name='buku'),
]
