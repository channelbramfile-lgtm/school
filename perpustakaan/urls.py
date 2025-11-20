from django.contrib import admin
from django.urls import path,include
from .views import dashboard, profil,kontak,alamat,sejarah,buku,tambah_buku,hapus_buku,edit_buku,    penulis,tambah_penulis,hapus_penulis,edit_penulis,view_penulis,    penebit,tambah_penebit,hapus_penebit,edit_penebit ,    pendidikan,tambah_pendidikan,hapus_pendidikan,edit_pendidikan


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
   path('edit-penulis/<int:idpenulis>',edit_penulis,name='edit_penulis'),
   path('view-detail-penulis/<int:id>',view_penulis,name='view_penulis'),

   path('penebit/',penebit,name='penebit'),
   path('tambah_penebit/',tambah_penebit,name='tambah_penebit'),
   path('hapus-data-penebit/<int:idpenebit>',hapus_penebit,name='hapus_penebit'),
   path('edit-penebit/<int:idpenebit>',edit_penebit,name='edit_penebit'),

   path('pendidikan/',pendidikan,name='pendidikan'),
   path('tambah_pendidikan/',tambah_pendidikan,name='tambah_pendidikan'),
   path('hapus-data-pendidikan/<int:idpendidikan>',hapus_pendidikan,name='hapus_pendidikan'),
   path('edit-pendidikan/<int:idpendidikan>',edit_pendidikan,name='edit_pendidikan'),
]
