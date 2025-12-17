from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import CustomUser, Buku, Penulis, Penebit, Pendidikan, HistoryPendidikan, Sekolah, SumberDayaManusia,Devisi,PembelianBuku, PeminjamanBuku
from django.forms.widgets import NumberInput








#class form

class CreateCustomeUser(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput)
    password1 = forms.CharField(label='Password',widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password',widget=forms.PasswordInput)
    
    class Meta:
        model = CustomUser
        fields = ['username','email','password1','password2']

    def clean(self):
        cleaned_data = super().clean()

        p1 = cleaned_data.get('password1')
        p2 = cleaned_data.get('password2')

        if p1 != p2:
            raise forms.ValidationError('Password tidak sesuai!')
        return cleaned_data
    
    def clean_email(self):
        cleaned_data = super().clean()

        email1 = cleaned_data.get('email')
        if CustomUser.objects.filter(email=email1):
            raise forms.ValidationError("Email Sudah Ada!")
        return email1

    def clean_username(self):
        cleaned_data = super().clean()

        username1 = cleaned_data.get('username')
        if CustomUser.objects.filter(username=username1):
            raise forms.ValidationError("username Sudah Ada!")
        return username1





class Tambah_Buku(forms.ModelForm):
    class Meta:
            model = Buku
            fields ='__all__'

class Tambah_Penulis(forms.ModelForm):
    class Meta:
            model = Penulis
            fields ='__all__'

class Tambah_Penebit(forms.ModelForm):
    class Meta:
            model = Penebit
            fields ='__all__'

class Tambah_Pendidikan(forms.ModelForm):
    class Meta:
            model = Pendidikan
            fields ='__all__'

class Tambah_History_Pendidikan(forms.ModelForm):
    class Meta:
            model = HistoryPendidikan
            fields =['pendidikan','sekolah']


class Edit_Buku(forms.ModelForm):
    class Meta:
            model = Buku
            fields ='__all__'

class Edit_Penulis(forms.ModelForm):
    class Meta:
            model = Penulis
            fields ='__all__'

class Edit_Penebit(forms.ModelForm):
    class Meta:
            model = Penebit
            fields ='__all__'

class Edit_Pendidikan(forms.ModelForm):
    class Meta:
            model = Pendidikan
            fields ='__all__'

class Tambah_Sekolah(forms.ModelForm):
    class Meta:
            model = Sekolah
            fields ='__all__'

class Edit_Sekolah(forms.ModelForm):
    class Meta:
            model = Sekolah
            fields ='__all__'

class Tambah_SumberDayaManusia(forms.ModelForm):
    class Meta:
            model = SumberDayaManusia
            fields ='__all__'
    tgllahir =forms.DateField(label='Tgl.Lahir',widget=NumberInput(attrs={'type':'date'}))

class Edit_SumberDayaManusia(forms.ModelForm):
    class Meta:
            model = SumberDayaManusia
            fields ='__all__'
    tgllahir =forms.DateField(label='Tgl.Lahir',widget=NumberInput(attrs={'type':'date'}))


class Edit_Devisi(forms.ModelForm):
    class Meta:
            model = Devisi
            fields ='__all__'

class Tambah_Devisi(forms.ModelForm):
    class Meta:
            model = Devisi
            fields ='__all__'

class Edit_PembelianBuku(forms.ModelForm):
    class Meta:
            model = PembelianBuku
            fields ='__all__'

class Tambah_PembelianBuku(forms.ModelForm):
    class Meta:
            model = PembelianBuku
            fields ='__all__'

class UbahStatusPeminjaman(forms.ModelForm):
      class Meta:
            model = PeminjamanBuku
            fields=['status']


