from django.db import models

# Create your models here.
class Buku(models.Model):
    bukuId          = models.CharField(max_length=50,null=False,blank=False,verbose_name="Buku ID")
    judul           = models.CharField(max_length=250,null=False,blank=False,verbose_name="Judul")
    isbn            = models.CharField(max_length=50,null=True,blank=True,verbose_name="ISBN")
    tahunTerbit     = models.CharField(max_length=20,null=True,blank=True,verbose_name="Tahun Terbit")
    sinopsi         = models.TextField(null=False,blank=False,verbose_name="Sinopsis")
    foto = models.ImageField(upload_to='foto_buku',null=True,blank=True)
    created_at       = models.DateTimeField(auto_now_add=True)
    update_at        = models.DateTimeField(auto_now=True)

    def __str__(self):
       return self.judul

class Pendidikan(models.Model):
 pendidikanID               = models.CharField(max_length=50,null=False,blank=False,verbose_name="Pendidikan ID")  
 jenjang             = models.CharField(max_length=50,null=False,blank=False,verbose_name="Jenjang Pendidikan")
 namasingkatan             = models.CharField(max_length=50,null=False,blank=False,verbose_name="Singkatan")   
 created_at       = models.DateTimeField(auto_now_add=True)
 update_at        = models.DateTimeField(auto_now=True)
 def __str__(self):
       return self.jenjang
    
class Penulis(models.Model):
    penulisId               = models.CharField(max_length=50,null=False,blank=False,verbose_name="Penulis ID")
    namapenulis             = models.CharField(max_length=200,null=False,blank=False,verbose_name="Nama Penulis")
    jkelamin =(
        ('PRIA','PRIA'),
        ('WANITA','WANITA'),
    )
    jk                      = models.CharField(max_length=50,choices=jkelamin,null=True,blank=True,verbose_name="Jenis Kelamin")
    
    instagram                = models.CharField(max_length=50,null=True,blank=True,verbose_name="Instagram")

    foto = models.ImageField(upload_to='foto_penulis',null=True,blank=True)
    
    created_at       = models.DateTimeField(auto_now_add=True)
    update_at        = models.DateTimeField(auto_now=True)
    def __str__(self):
       return self.namapenulis

class Sekolah(models.Model):
    sekolahId = models.CharField(max_length=50,null=False,blank=False,verbose_name="Sekolah ID")
    namasekolah = models.CharField(max_length=50,null=False,blank=False,verbose_name="Nama Sekolah")
    created_at       = models.DateTimeField(auto_now_add=True)
    update_at        = models.DateTimeField(auto_now=True)
    def __str__(self):
       return self.namasekolah

class HistoryPendidikan(models.Model):
    penulis              = models.ForeignKey(Penulis,on_delete=models.CASCADE,null=True,blank=True, verbose_name='Penulis')
    pendidikan           = models.ForeignKey(Pendidikan,on_delete=models.CASCADE,null=True,blank=True, verbose_name='Pendidikan')
    sekolah           = models.ForeignKey(Sekolah,on_delete=models.CASCADE,null=True,blank=True, verbose_name='Sekolah')
    created_at       = models.DateTimeField(auto_now_add=True)
    update_at        = models.DateTimeField(auto_now=True)
   
class Penebit(models.Model):
    penebitId          = models.CharField(max_length=50,null=False,blank=False,verbose_name="Penerbit ID")
    namapenebit          = models.CharField(max_length=250,null=False,blank=False,verbose_name="Nama Penerbit")
    created_at       = models.DateTimeField(auto_now_add=True)
    update_at        = models.DateTimeField(auto_now=True)
    def __str__(self):
       return self.namapenebit
    
class Devisi(models.Model):
 devisiID               = models.CharField(max_length=50,null=False,blank=False,verbose_name="Devisi ID")  
 devisi            = models.CharField(max_length=50,null=False,blank=False,verbose_name="Devisi")
 namasingkatan             = models.CharField(max_length=50,null=False,blank=False,verbose_name="Singkatan")   
 created_at       = models.DateTimeField(auto_now_add=True)
 update_at        = models.DateTimeField(auto_now=True)
 def __str__(self):
       return self.devisi
    
class SumberDayaManusia(models.Model):
    nik              = models.CharField(max_length=50,null=False,blank=False,verbose_name="No. Induk Kepegawaian")  
    nama             = models.CharField(max_length=200,null=False,blank=False,verbose_name="Nama Lengkap")
    jkelamin =(
        ('PRIA','PRIA'),
        ('WANITA','WANITA'),
    )
    jk                      = models.CharField(max_length=50,choices=jkelamin,null=True,blank=True,verbose_name="Jenis Kelamin")
    nohp             = models.CharField(max_length=50,null=False,blank=False,verbose_name="No. Hp")   
    tgllahir             = models.DateField(verbose_name="Tanggal Lahir")
    tempatlahir            = models.CharField(max_length=200,null=False,blank=False,verbose_name="Tempat Lahir")
    alamat         = models.TextField(null=False,blank=False,verbose_name="Alamat")
    pendidikan           = models.ForeignKey(Pendidikan,on_delete=models.CASCADE,null=True,blank=True, verbose_name='Pendidikan')
    devisi           = models.ForeignKey(Devisi,on_delete=models.CASCADE,null=True,blank=True, verbose_name='Devisi')
    foto = models.ImageField(upload_to='foto_penulis',null=True,blank=True)
    created_at       = models.DateTimeField(auto_now_add=True)
    update_at        = models.DateTimeField(auto_now=True)

    def __str__(self):
       return self.nik
    
class PembelianBuku(models.Model):
    pembelianbukuId = models.CharField(max_length=50,null=False,blank=False,verbose_name="Pembelian Buku ID")
    judul           = models.CharField(max_length=250,null=False,blank=False,verbose_name="Judul")
    isbn            = models.CharField(max_length=50,null=True,blank=True,verbose_name="ISBN")
    tahunTerbit     = models.CharField(max_length=20,null=True,blank=True,verbose_name="Tahun Terbit")
    sinopsi         = models.TextField(null=False,blank=False,verbose_name="Sinopsis")
    kuantitas       = models.IntegerField(max_length=250,null=False,blank=False,verbose_name="Kuantitas")
    harga           = models.FloatField(max_length=250,null=False,blank=False,verbose_name="Harga")

    foto = models.ImageField(upload_to='foto_buku',null=True,blank=True)

    created_at       = models.DateTimeField(auto_now_add=True)
    update_at        = models.DateTimeField(auto_now=True)

    def __str__(self):
       return self.judul
    

