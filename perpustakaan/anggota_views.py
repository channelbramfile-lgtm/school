from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import PeminjamanBuku ,CustomUser,Buku,Penulis,Penebit ,Pendidikan,HistoryPendidikan , Sekolah, SumberDayaManusia, Devisi, PembelianBuku
from .forms import CreateCustomeUser,Tambah_PembelianBuku, Edit_PembelianBuku, Tambah_Devisi , Edit_Devisi, Tambah_SumberDayaManusia , Edit_SumberDayaManusia, Tambah_History_Pendidikan, Tambah_Buku, Edit_Buku, Tambah_Sekolah, Edit_Sekolah, Tambah_Penulis , Edit_Penulis, Tambah_Penebit , Edit_Penebit , Tambah_Pendidikan , Edit_Pendidikan
from django.contrib import messages
from perpustakaan.EmailBackEnd import EmailBackEnd

from django.contrib.auth import authenticate,login,logout

from django.utils import timezone
from datetime import timedelta




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

def anggota_view_buku(request,idbuku):
     buku = Buku.objects.filter(id = idbuku).first()
    
     context={
       'buku':buku,
       'title':'View Buku',
      
    }
    
   
     return render(request,'anggota/view_buku.html',context) 


def list_buku(request):

     #select from buku 
    buku = Buku.objects.all()

    context={
       'buku':buku,
        'title':'List Buku' 
       
    }
    
   
    return render(request,'anggota/buku.html',context)

def anggota_pinjam_buku(request,id):
    buku =Buku.objects.filter(id=id).first()
    sudah_pinjam = PeminjamanBuku.objects.filter(
        customuser = request.user.id,
        buku=buku,
        tanggal_pengembalian__isnull = True

    ).exists()

    if sudah_pinjam:
        messages.warning(request,'Kamu Masih Meminjam Buku ini dan belum di kembalikan.')
        return redirect('daftar_peminjaman_buku')
    tgl_pinjam = timezone.localdate() # mengambil waktu sekarang sesuai timezone
    tgl_batas = tgl_pinjam + timedelta(days=7) #menambahkan 7 hari dari tgl pinjam

    PeminjamanBuku.objects.create(
        customuser = request.user,
        buku = buku,
        tanggal_pinjam = tgl_pinjam,
        tanggal_batas_peminjaman = tgl_batas,
        tanggal_pengembalian = None
    )
    buku.stok -=1
    buku.save(update_fields=['stok'])


    messages.success(request,f'Buku{buku.judul} berhasil di pinjam')
    return redirect('daftar_peminjaman_buku')
    

def daftar_peminjaman_buku(request):
    id = request.user.id #mengambil id user yang login

    user = CustomUser.objects.filter(id=id).first() # ambil id sesuai user yang login
    daftar_buku = PeminjamanBuku.objects.filter(customuser_id=user) # menmapikan data peminjaman buku sesua user yang login
    today = timezone.now().date()


    for a in daftar_buku:
        if a.tanggal_pinjam:
            # total hari dari tanggal pinjam sampai hari ini
            a.total_hari = (today - a.tanggal_pinjam).days
        else:
            a.total_hari = 0

        # OPTIONAL: sisa hari sampai batas peminjaman
        if a.tanggal_batas_peminjaman:
            a.sisa_hari = (a.tanggal_batas_peminjaman - today).days
        else:
            a.sisa_hari = 0
    context ={
        'daftar':daftar_buku,
        'title':'DAFTAR PEMINJAMAN BUKU' 
    }
    return render(request,'anggota/daftar_peminjaman_buku.html',context) 

def logout_anggota(request):
    logout(request)
    return redirect('loginPage')


