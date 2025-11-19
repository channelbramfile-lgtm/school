from django.contrib import admin
from django.urls import path,include
from .views import dashboard, profil,kontak,alamat,sejarah,buku,tambah_buku,hapus_buku,edit_buku,penulis,tambah_penulis,hapus_penulis

urlpatterns = [
   path('',dashboard,name='dashboard'),
   path('profil/',profil,name='profil'),
   path('kontak/',kontak,name='kontak'),
   path('alamat/',alamat,name='alamat'),
   path('sejarah/',sejarah,name='sejarah'),
   
   path('buku/',buku,name='buku'),
   path('tambah_buku/',tambah_buku,name='tambah_buku'),
   path('hapus-data-buku/<int:idbuku>',hapus_buku,name='hapus_buku'),
   path('edit-buku/<int:idbuku>',edit_buku,name='edit_buku'),

   path('penulis/',penulis,name='penulis'),
   path('tambah_penulis/',tambah_penulis,name='tambah_penulis'),
   path('hapus-data-penulis/<int:idpenulis>',hapus_penulis,name='hapus_penulis'),
]
