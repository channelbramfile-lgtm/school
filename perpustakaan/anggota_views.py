from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import CustomUser,Buku,Penulis,Penebit ,Pendidikan,HistoryPendidikan , Sekolah, SumberDayaManusia, Devisi, PembelianBuku
from .forms import CreateCustomeUser,Tambah_PembelianBuku, Edit_PembelianBuku, Tambah_Devisi , Edit_Devisi, Tambah_SumberDayaManusia , Edit_SumberDayaManusia, Tambah_History_Pendidikan, Tambah_Buku, Edit_Buku, Tambah_Sekolah, Edit_Sekolah, Tambah_Penulis , Edit_Penulis, Tambah_Penebit , Edit_Penebit , Tambah_Pendidikan , Edit_Pendidikan
from django.contrib import messages
from perpustakaan.EmailBackEnd import EmailBackEnd

from django.contrib.auth import authenticate,login,logout



# Create your views here.





def anggota_dashboard(request):

    JumlahBuku = Buku.objects.all().count()
    JumlahPenulis = Penulis.objects.all().count()
    listbuku = Buku.objects.all()[:4]
    context ={
        'jumlah':JumlahBuku,
        'jumlahpenulis':JumlahPenulis,
        'listbuku':listbuku,
    }
    return render(request,'anggota/anggota_dashboard.html',context)
