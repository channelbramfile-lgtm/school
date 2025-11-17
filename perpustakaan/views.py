from django.shortcuts import render
from django.http import HttpResponse
from .models import Buku
from .forms import Tambah_Buku


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
    #buku = Buku.objects.all()

    '''
    bukuId          = "BK01"
    judul           = "Belajar Django"
    isbn            = "123456"
    tahunTerbit     = "2025"
    sinopsi         = "buku yang menjelaskan"
    context={
    
        'bukuId':bukuId,
        'judul':judul,
        'isbn':isbn,
        'tahunTerbit':tahunTerbit,
        'sinopsi':sinopsi,
'''
    
   
    return render(request,'buku.html')
def tambah_buku(request):

    if request.method == 'POST':
        form =Tambah_Buku(request.POST)
        if form.is_valid():
            form.save()
    else:
        form =Tambah_Buku()
    context = {
        'form':form,
    }

    return render(request,'tambah_buku.html',context)