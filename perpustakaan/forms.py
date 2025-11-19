from django import forms
from .models import Buku, Penulis

#class form
class Tambah_Buku(forms.ModelForm):
    class Meta:
            model = Buku
            fields ='__all__'

class Tambah_Penulis(forms.ModelForm):
    class Meta:
            model = Penulis
            fields ='__all__'

class Edit_Buku(forms.ModelForm):
    class Meta:
            model = Buku
            fields ='__all__'


