from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Buku,Penulis
from .forms import Tambah_Buku, Edit_Buku, Tambah_Penulis
from django.contrib import messages


# Create your views here.

def dashboard(request):
    return render(request,'dashboard.html')
def profil(request):
    return render(request,'profil.html')
def kontak(request):
    return render(request,'kontak.html')
def alamat(request):
    return render(request,'alamat.html')
def sejarah(request):
    return render(request,'sejarah.html')

def buku(request):

     #select from buku 
    buku = Buku.objects.all()

    context={
       'buku':buku,
    }
    
   
    return render(request,'buku.html',context)

def tambah_buku(request):

    if request.method == 'POST':
        form =Tambah_Buku(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Data Berhasil Disimpan')
            return redirect('buku')
            
    else:
        form =Tambah_Buku()
    context = {
        'form':form,
    }

    return render(request,'tambah_buku.html',context)

def hapus_buku(request,idbuku):
    bukuid = Buku.objects.get(id = idbuku)
    bukuid.delete()
    messages.success(request,'Data Berhasil Dihapus')
    return redirect('buku')

def penulis(request):

     #select from penulis 
    penulis = Penulis.objects.all()

    context={
       'penulis':penulis,
    }
    
   
    return render(request,'penulis.html',context)

def tambah_penulis(request):

    if request.method == 'POST':
        form =Tambah_Penulis(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Data Berhasil Disimpan')
            return redirect('penulis')
            
    else:
        form =Tambah_Penulis()
    context = {
        'form':form,
    }

    return render(request,'tambah_penulis.html',context)

def hapus_penulis(request,idpenulis):
    penulisid = Penulis.objects.get(id = idpenulis)
    penulisid.delete()
    messages.success(request,'Data Berhasil Dihapus')
    return redirect('penulis')

def edit_buku(request,idbuku):
    bukuid = Buku.objects.get(id = idbuku)
    ambildata = Buku.objects.filter(id = idbuku).first()
    if request.method =="POST":
        form =Edit_Buku(request.POST, instance=ambildata)
        if form.is_valid():
            form.save()
            messages.success(request,'Data Berhasil DiPerbaharui')
            return redirect('buku')
    else:
        form =Edit_Buku(instance=ambildata)
    context = {
        'form':form,
    }

    return render(request,'Edit_buku.html',context)
