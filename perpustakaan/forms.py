from django import forms
from .models import Buku, Penulis, Penebit, Pendidikan

#class form
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


