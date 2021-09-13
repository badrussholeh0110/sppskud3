from django import forms
from django.db.models import fields
from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm

class PetugasForm(ModelForm):
    class Meta:
        model = Petugas
        fields = '__all__'
        exclude = ['level']
        widgets = {
            'namapetugas': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'nama petugas'}),
            'namaunit': forms.Select(attrs={'class': 'form-control'}),

        }
        lebels = {
            'nama':'Nama',
        }

class PeternakForm(ModelForm):
    class Meta:
        model = Peternak
        fields = '__all__'
        exclude = ['level']
        widgets = {
            'nama': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'nama peternak'}),
            'alamat': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'alamat peternak'}),
            'namaunit': forms.Select(attrs={'class': 'form-control'}),

        }
        lebels = {
            'nama':'Nama',
        }

class UnitForm(ModelForm):
    class Meta:
        model = Unit
        fields = '__all__'
        widgets = {
            'namaunit': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'nama unit'}),
            'alamatunit': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'alamat unit'}),
            

        }
        lebels = {
            'nama':'Nama',
        }

class SetoranForm(ModelForm):
    class Meta:
        model = Setoran
        fields = '__all__'
        widgets = {
            'namaunit': forms.Select(attrs={'class': 'form-control'}),
            'nama': forms.Select(attrs={'class': 'form-control'}),
            'jumlahsetoran': forms.TextInput(attrs={'class': 'form-control'}),
            'harga': forms.Select(attrs={'class': 'form-control'}),
            'namapetugas': forms.Select(attrs={'class': 'form-control'}),
            'tgl': forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
        labels = {
            'namaunit':'Nama Unit',
            'nama':'Nama Peternak',
            'jumlahsetoran':'Jumlah Setoran',
            'harga':'Harga',
            'namapetugas':'Petugas',
            'tgl':'Tgl',
        }

class HargaForm(ModelForm):
    class Meta:
        model = Harga
        fields = '__all__'
        widgets = {
            'harga': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'harga per 1 liter'}),
        }
        labels = {
            'nama':'Nama',
        }

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ID Petugas'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nama'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'value': 'petugas', 'readonly': 'True'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'username': 'ID Petugas',
            'first_name': 'Nama Petugas',
            'last_name': 'Level',
        }

class UserpeternakForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name','email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ID peternak'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nama'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'value': 'peternak', 'readonly': 'True'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'username': 'ID peternak',
            'first_name': 'Nama peternak',
            'last_name': 'Level',
        }

class UuserForm(UserCreationForm):
    class Meta:
        model= User
        fields = ['username', 'first_name', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'True'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'True'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'password1': forms.TextInput(attrs={'class': 'form-control'}),
            'password2': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'username': 'ID peternak',
            'first_name': 'Nama peternak',
        }

class UuserForm1(UserCreationForm):
    class Meta:
        model= User
        fields = ['username', 'first_name', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'True'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'True'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'password1': forms.TextInput(attrs={'class': 'form-control'}),
            'password2': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'username': 'ID admin',
            'first_name': 'Nama admin',
        }