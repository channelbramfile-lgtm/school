from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Buku,Penulis,Penebit ,Pendidikan,HistoryPendidikan , Sekolah
from .forms import Tambah_History_Pendidikan, Tambah_Buku, Edit_Buku, Tambah_Sekolah, Edit_Sekolah, Tambah_Penulis , Edit_Penulis, Tambah_Penebit , Edit_Penebit , Tambah_Pendidikan , Edit_Pendidikan
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
        form =Tambah_Buku(request.POST,request.FILES)
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

def view_buku(request,idbuku):
     buku = Buku.objects.filter(id = idbuku).first()
    
     context={
       'buku':buku,
      
    }
    
   
     return render(request,'view_buku.html',context) 







def penulis(request):

     #select from penulis 
    penulis = Penulis.objects.all()

    context={
       'penulis':penulis,
    }
    
   
    return render(request,'penulis.html',context)

def tambah_penulis(request):

    if request.method == 'POST':
        form =Tambah_Penulis(request.POST,request.FILES)
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

def edit_penulis(request,idpenulis):
    penulisid = Penulis.objects.get(id = idpenulis)
    ambildata = Penulis.objects.filter(id = idpenulis).first()
    if request.method =="POST":
        form =Edit_Penulis(request.POST, instance=ambildata)
        if form.is_valid():
            form.save()
            messages.success(request,'Data Berhasil DiPerbaharui')
            return redirect('penulis')
    else:
        form =Edit_Penulis(instance=ambildata)
    context = {
        'form':form,
    }

    return render(request,'Edit_penulis.html',context)







def penebit(request):

     #select from penebit
    penebit = Penebit.objects.all()

    context={
       'penebit':penebit,
    }
    
   
    return render(request,'penebit.html',context)

def tambah_penebit(request):

    if request.method == 'POST':
        form =Tambah_Penebit(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Data Berhasil Disimpan')
            return redirect('penebit')
            
    else:
        form =Tambah_Penebit()
    context = {
        'form':form,
    }

    return render(request,'tambah_penebit.html',context)

def hapus_penebit(request,idpenebit):
    penebitid = Penebit.objects.get(id = idpenebit)
    penebitid.delete()
    messages.success(request,'Data Berhasil Dihapus')
    return redirect('penebit')

def edit_penebit(request,idpenebit):
    penebitid = Penebit.objects.get(id = idpenebit)
    ambildata = Penebit.objects.filter(id = idpenebit).first()
    if request.method =="POST":
        form =Edit_Penebit(request.POST, instance=ambildata)
        if form.is_valid():
            form.save()
            messages.success(request,'Data Berhasil DiPerbaharui')
            return redirect('penebit')
    else:
        form =Edit_Penebit(instance=ambildata)
    context = {
        'form':form,
    }

    return render(request,'Edit_penebit.html',context)





def pendidikan(request):

     #select from pendidikan
    pendidikan = Pendidikan.objects.all()

    context={
       'pendidikan':pendidikan,
    }
    
   
    return render(request,'pendidikan.html',context)

def tambah_pendidikan(request):

    if request.method == 'POST':
        form =Tambah_Pendidikan(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Data Berhasil Disimpan')
            return redirect('pendidikan')
            
    else:
        form =Tambah_Pendidikan()
    context = {
        'form':form,
    }

    return render(request,'tambah_pendidikan.html',context)

def hapus_pendidikan(request,idpendidikan):
    pendidikanid = Pendidikan.objects.get(id = idpendidikan)
    pendidikanid.delete()
    messages.success(request,'Data Berhasil Dihapus')
    return redirect('pendidikan')

def edit_pendidikan(request,idpendidikan):
    pendidikanid = Pendidikan.objects.get(id = idpendidikan)
    ambildata = Pendidikan.objects.filter(id = idpendidikan).first()
    if request.method =="POST":
        form =Edit_Pendidikan(request.POST, instance=ambildata)
        if form.is_valid():
            form.save()
            messages.success(request,'Data Berhasil DiPerbaharui')
            return redirect('pendidikan')
    else:
        form =Edit_Pendidikan(instance=ambildata)
    context = {
        'form':form,
    }

    return render(request,'Edit_pendidikan.html',context)

def view_penulis(request,id):
     view = Penulis.objects.filter(id = id).first()
     history =HistoryPendidikan.objects.filter(penulis_id = id)
     context={
       'view':view,
       'history':history,
    }
    
   
     return render(request,'view_penulis.html',context)

def tambah_history_pendidikan(request,idpenulis):

    #select * from penulis where id= idpenulis

    penulisid= Penulis.objects.get(id=idpenulis)
    
    if request.method =="POST":
        form = Tambah_History_Pendidikan(request.POST)
        if form.is_valid():
            writer = form.save(commit=False)
            writer.penulis_id = penulisid.id
            form.save()
            messages.success(request,'Data Pendidikan Berhasil Ditambah')
            return redirect('view_penulis',id=penulisid.id)
    else:
        form = Tambah_History_Pendidikan()
        
    context= {
            'form':form,
        }
    return render(request,'tambah_history_pendidikan.html',context)    



def sekolah(request):

     #select from sekolah 
    sekolah = Sekolah.objects.all()

    context={
       'sekolah':sekolah,
    }
    
   
    return render(request,'sekolah.html',context)

def tambah_sekolah(request):

    if request.method == 'POST':
        form =Tambah_Sekolah(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Data Berhasil Disimpan')
            return redirect('sekolah')
            
    else:
        form =Tambah_Sekolah()
    context = {
        'form':form,
    }

    return render(request,'tambah_sekolah.html',context)

def hapus_sekolah(request,idsekolah):
    sekolahid = Sekolah.objects.get(id = idsekolah)
    sekolahid.delete()
    messages.success(request,'Data Berhasil Dihapus')
    return redirect('sekolah')

def edit_sekolah(request,idsekolah):
    sekolahid = Sekolah.objects.get(id = idsekolah)
    ambildata = Sekolah.objects.filter(id = idsekolah).first()
    if request.method =="POST":
        form =Edit_Sekolah(request.POST, instance=ambildata)
        if form.is_valid():
            form.save()
            messages.success(request,'Data Berhasil DiPerbaharui')
            return redirect('sekolah')
    else:
        form =Edit_Sekolah(instance=ambildata)
    context = {
        'form':form,
    }

    return render(request,'Edit_sekolah.html',context)
