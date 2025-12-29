from django.contrib import admin
from django.urls import path,include
from .admin_views import  peminjaman_filter_pinjam, laporan_rekap_anggota_pdf, rekap_anggota,rekap_anggota_pinjam, ubah_status_peminjaman,list_peminjan_buku,logout_user, tambah_user_anggota, manage_akun_anggota, doLogin, loginPage, pembelianbuku,tambah_pembelianbuku,hapus_pembelianbuku,edit_pembelianbuku,view_pembelianbuku,   devisi,tambah_devisi,hapus_devisi,edit_devisi ,sdm,tambah_sdm,hapus_sdm,edit_sdm,view_sdm, sekolah,tambah_sekolah,hapus_sekolah,edit_sekolah, admin_dashboard, profil,kontak,alamat,sejarah,buku,tambah_buku,hapus_buku,edit_buku,view_buku,    penulis,tambah_penulis,hapus_penulis,edit_penulis,view_penulis,    penebit,tambah_penebit,hapus_penebit,edit_penebit ,    pendidikan,tambah_pendidikan,hapus_pendidikan,edit_pendidikan ,tambah_history_pendidikan

from .anggota_views import anggota_dashboard,anggota_view_buku,list_buku,anggota_pinjam_buku,daftar_peminjaman_buku,logout_anggota, laporan_peminjaman_pdf
urlpatterns = [
    
   path('',loginPage,name='loginPage'),
   path('doLogin/',doLogin, name="doLogin"),
   path('logout_user/',logout_user, name="logout_user"),

   #halaman admin
   path('admin_dashboard/',admin_dashboard,name='admin_dashboard'),
   path('profil/',profil,name='profil'),

   path('manage_akun_anggota/',manage_akun_anggota,name='manage_akun_anggota'),
   path('tambah_user_anggota/',tambah_user_anggota,name='tambah_user_anggota'),


   path('kontak/',kontak,name='kontak'),
   path('alamat/',alamat,name='alamat'),
   path('sejarah/',sejarah,name='sejarah'),
   
   path('buku/',buku,name='buku'),
   path('tambah_buku/',tambah_buku,name='tambah_buku'),
   path('hapus-data-buku/<int:idbuku>',hapus_buku,name='hapus_buku'),
   path('edit-buku/<int:idbuku>',edit_buku,name='edit_buku'),
   path('view-buku/<int:idbuku>',view_buku,name='view_buku'),

   path('sekolah/',sekolah,name='sekolah'),
   path('tambah_sekolah/',tambah_sekolah,name='tambah_sekolah'),
   path('hapus-data-sekolah/<int:idsekolah>',hapus_sekolah,name='hapus_sekolah'),
   path('edit-sekolah/<int:idsekolah>',edit_sekolah,name='edit_sekolah'),

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
   path('tambah_history_pendidikan/<int:idpenulis>',tambah_history_pendidikan,name='tambah_history_pendidikan'),
   path('tambah_pendidikan/',tambah_pendidikan,name='tambah_pendidikan'),
   path('hapus-data-pendidikan/<int:idpendidikan>',hapus_pendidikan,name='hapus_pendidikan'),
   path('edit-pendidikan/<int:idpendidikan>',edit_pendidikan,name='edit_pendidikan'),

   path('sdm/',sdm,name='sdm'),
   path('tambah_sdm/',tambah_sdm,name='tambah_sdm'),
   path('hapus-data-sdm/<int:idsdm>',hapus_sdm,name='hapus_sdm'),
   path('edit-sdm/<int:idsdm>',edit_sdm,name='edit_sdm'),
   path('view-sdm/<int:idsdm>',view_sdm,name='view_sdm'),
   # path('view-detail-sdm/<int:id>',view_sdm,name='view_sdm'),


   path('devisi/',devisi,name='devisi'),
   
   path('tambah_devisi/',tambah_devisi,name='tambah_devisi'),
   path('hapus-data-devisi/<int:iddevisi>',hapus_devisi,name='hapus_devisi'),
   path('edit-devisi/<int:iddevisi>',edit_devisi,name='edit_devisi'),


   path('pembelianbuku/',pembelianbuku,name='pembelianbuku'),
   path('tambah_pembelianbuku/',tambah_pembelianbuku,name='tambah_pembelianbuku'),
   path('hapus-data-pembelianbuku/<int:idpembelianbuku>',hapus_pembelianbuku,name='hapus_pembelianbuku'),
   path('edit-pembelianbuku/<int:idpembelianbuku>',edit_pembelianbuku,name='edit_pembelianbuku'),
   path('view-pembelianbuku/<int:idpembelianbuku>',view_pembelianbuku,name='view_pembelianbuku'),


   path('daftar/peminjam/buku',list_peminjan_buku,name='list_peminjan_buku'),

     path('rekap/peminjaman/buku',rekap_anggota_pinjam,name='rekap_anggota_pinjam'),

    #path('admin/peminjaman/<int:id>/ubah-status/',ubah_status_peminjaman,name='ubah_status_peminjaman'),
    path('admin_home/peminjaman/<int:id>/ubah-status/',ubah_status_peminjaman,name='ubah_status_peminjaman'),

    path('rekap_anggota/',rekap_anggota,name='rekap_anggota'),

     path('laporan/rekap-anggota/pdf/', laporan_rekap_anggota_pdf, name='laporan_rekap_anggota_pdf'),

    path("peminjaman/filter-tanggal-pinjam/", peminjaman_filter_pinjam,name='peminjaman_filter_pinjam'),


   #halaman anggota
   path('anggota_dashboard/',anggota_dashboard,name='anggota_dashboard'),
   path('anggota_view_buku/<int:idbuku>',anggota_view_buku,name='anggota_view_buku'),
   path('anggota_list_buku/',list_buku,name='anggota_list_buku'),

    path('anggota/buku/<int:id>/pinjam',anggota_pinjam_buku,name='anggota_pinjam_buku'),

    path('daftar_peminjaman_buku/',daftar_peminjaman_buku,name='daftar_peminjaman_buku'),

    path('logout_anggota/',logout_anggota, name="logout_anggota"),

    # Tambahkan di urlpatterns
path('anggota/laporan-pdf/', laporan_peminjaman_pdf, name='laporan_peminjaman_pdf'),
]  
