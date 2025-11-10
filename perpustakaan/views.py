from django.shortcuts import render
from django.http import HttpResponse


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
    return render(request,'buku.html')