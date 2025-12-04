from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Buku,Penulis,Penebit ,Pendidikan,HistoryPendidikan , Sekolah, SumberDayaManusia, Devisi, PembelianBuku
from .forms import Tambah_PembelianBuku, Edit_PembelianBuku, Tambah_Devisi , Edit_Devisi, Tambah_SumberDayaManusia , Edit_SumberDayaManusia, Tambah_History_Pendidikan, Tambah_Buku, Edit_Buku, Tambah_Sekolah, Edit_Sekolah, Tambah_Penulis , Edit_Penulis, Tambah_Penebit , Edit_Penebit , Tambah_Pendidikan , Edit_Pendidikan
from django.contrib import messages


# Create your views here.

def dashboard(request):

    JumlahBuku = Buku.objects.all().count()
    JumlahPenulis = Penulis.objects.all().count()

    context ={
        'jumlah':JumlahBuku,
        'jumlahpenulis':JumlahPenulis,
    }
    return render(request,'dashboard.html',context)
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
        'title':'Manage Buku',
       
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
        form =Edit_Buku(request.POST,request.FILES, instance=ambildata)
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
        form =Edit_Penulis(request.POST ,request.FILES , instance=ambildata)
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














def sdm(request):

     #select from sdm 
    sdm = SumberDayaManusia.objects.all()

    context={
       'sdm':sdm,
    }
    
   
    return render(request,'sdm.html',context)

def tambah_sdm(request):

    if request.method == 'POST':
        form =Tambah_SumberDayaManusia(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,'Data Berhasil Disimpan')
            return redirect('sdm')
            
    else:
        form =Tambah_SumberDayaManusia()
    context = {
        'form':form,
    }

    return render(request,'tambah_sdm.html',context)

def hapus_sdm(request,idsdm):
    sdmid = SumberDayaManusia.objects.get(id = idsdm)
    sdmid.delete()
    messages.success(request,'Data Berhasil Dihapus')
    return redirect('sdm')

def edit_sdm(request,idsdm):
    sdmid = SumberDayaManusia.objects.get(id = idsdm)
    ambildata = SumberDayaManusia.objects.filter(id = idsdm).first()
    if request.method =="POST":
        form =Edit_SumberDayaManusia(request.POST ,request.FILES , instance=ambildata)
        if form.is_valid():
            form.save()
            messages.success(request,'Data Berhasil DiPerbaharui')
            return redirect('sdm')
    else:
        form =Edit_SumberDayaManusia(instance=ambildata)
    context = {
        'form':form,
    }

    return render(request,'Edit_sdm.html',context)

def view_sdm(request,idsdm):
     sdm = SumberDayaManusia.objects.filter(id = idsdm).first()
    
     context={
       'sdm':sdm,
      
    }
    
   
     return render(request,'view_sdm.html',context) 


def devisi(request):

     #select from Devisi
    devisi = Devisi.objects.all()

    context={
       'devisi':devisi,
    }
    
   
    return render(request,'devisi.html',context)

def tambah_devisi(request):

    if request.method == 'POST':
        form =Tambah_Devisi(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Data Berhasil Disimpan')
            return redirect('devisi')
            
    else:
        form =Tambah_Devisi()
    context = {
        'form':form,
    }

    return render(request,'tambah_devisi.html',context)

def hapus_devisi(request,iddevisi):
    devisiid = Devisi.objects.get(id = iddevisi)
    devisiid.delete()
    messages.success(request,'Data Berhasil Dihapus')
    return redirect('devisi')

def edit_devisi(request,iddevisi):
    devisiid = Devisi.objects.get(id = iddevisi)
    ambildata = Devisi.objects.filter(id = iddevisi).first()
    if request.method =="POST":
        form =Edit_Devisi(request.POST, instance=ambildata)
        if form.is_valid():
            form.save()
            messages.success(request,'Data Berhasil DiPerbaharui')
            return redirect('devisi')
    else:
        form =Edit_Devisi(instance=ambildata)
    context = {
        'form':form,
    }

    return render(request,'Edit_devisi.html',context)











def pembelianbuku(request):

     #select from pembelianbuku 
    pembelianbuku = PembelianBuku.objects.all()

    context={
       'pembelianbuku':pembelianbuku,
    }
    
   
    return render(request,'pembelianbuku.html',context)

def tambah_pembelianbuku(request):

    if request.method == 'POST':
        form =Tambah_PembelianBuku(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,'Data Berhasil Disimpan')
            return redirect('pembelianbuku')
            
    else:
        form =Tambah_PembelianBuku()
    context = {
        'form':form,
    }

    return render(request,'tambah_pembelianbuku.html',context)

def hapus_pembelianbuku(request,idpembelianbuku):
    pembelianbukuid = PembelianBuku.objects.get(id = idpembelianbuku)
    pembelianbukuid.delete()
    messages.success(request,'Data Berhasil Dihapus')
    return redirect('pembelianbuku')

def edit_pembelianbuku(request,idpembelianbuku):
    pembelianbukuid = PembelianBuku.objects.get(id = idpembelianbuku)
    ambildata = PembelianBuku.objects.filter(id = idpembelianbuku).first()
    if request.method =="POST":
        form =Edit_PembelianBuku(request.POST,request.FILES, instance=ambildata)
        if form.is_valid():
            form.save()
            messages.success(request,'Data Berhasil DiPerbaharui')
            return redirect('pembelianbuku')
    else:
        form =Edit_PembelianBuku(instance=ambildata)
    context = {
        'form':form,
    }

    return render(request,'Edit_pembelianbuku.html',context)

def view_pembelianbuku(request,idpembelianbuku):
     pembelianbuku = PembelianBuku.objects.filter(id = idpembelianbuku).first()
    
     context={
       'pembelianbuku':pembelianbuku,
      
    }
    
   
     return render(request,'view_pembelianbuku.html',context) 





