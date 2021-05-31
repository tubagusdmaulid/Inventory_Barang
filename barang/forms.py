from django.forms import ModelForm
from django import forms
from perpustakaan.models import Akun, Barang

class FormBarang(ModelForm):
    class Meta:
        model = Barang
        # fields = '__all__' = semua fields
        fields = '__all__'
        # # kecuali
        exclude = ['total_price'] 

        widgets = {
            'nama_barang': forms.TextInput({'class':'form-control'}),
            'stock': forms.NumberInput({'class':'form-control'}),
            'gedung_id': forms.TextInput({'class':'form-control'}),
            'ruang_id': forms.TextInput({'class':'form-control'}),
            'price': forms.NumberInput({'class':'form-control'}),
            'satuan': forms.NumberInput({'class':'form-control'}),
            'merek': forms.TextInput({'class':'form-control'}),
        }

class FormAkun(ModelForm):
    class Meta:
        model = Akun
        # fields = '__all__' = semua fields
        fields = '__all__'
        # # kecuali
        # exclude = ['total_price'] 

        widgets = {
            'email': forms.TextInput({'class':'form-control'}),
            'password': forms.TextInput({'class':'form-control'}),
            'role': forms.TextInput({'class':'form-control'}),
            'nama_pegawai': forms.TextInput({'class':'form-control'}),
            'nip': forms.NumberInput({'class':'form-control'}),
            'alamat': forms.TextInput({'class':'form-control'}),
            'telepon': forms.TextInput({'class':'form-control'}),
        }