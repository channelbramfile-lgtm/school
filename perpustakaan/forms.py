from django import forms
from .models import Buku, Penulis, Penebit, Pendidikan, HistoryPendidikan, Sekolah

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


