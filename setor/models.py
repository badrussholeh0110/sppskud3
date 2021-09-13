from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Unit(models.Model):
    id = models.IntegerField(primary_key=True)
    namaunit = models.CharField(max_length=200, blank=True, null=True)
    alamatunit = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return '%s, %s' % (self.namaunit, self.alamatunit)

class Petugas(models.Model):
    namapetugas = models.CharField(max_length=200, blank=True, null=True)
    namaunit = models.ForeignKey(Unit, null=True, on_delete=models.SET_NULL)
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    level = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return '%s, %s' % (self.namapetugas, self.namaunit)    

class Peternak(models.Model):
    id = models.IntegerField(primary_key=True)
    nama = models.CharField(max_length=200, blank=True, null=True)
    alamat = models.CharField(max_length=200, blank=True, null=True)
    namaunit = models.ForeignKey(Unit, null=True, on_delete=models.SET_NULL)
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    level = models.CharField(max_length=200, blank=True, null=True)


    def __str__(self):
        return self.nama

class Harga(models.Model):
    harga = models.IntegerField(null=True)
    tgl = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return '%s' % (self.harga)

class Setoran(models.Model):
    namapetugas = models.ForeignKey(Petugas, null=True, on_delete=models.SET_NULL)
    namaunit = models.ForeignKey(Unit, null=True, on_delete=models.SET_NULL)
    nama = models.ForeignKey(Peternak, null=True, on_delete=models.SET_NULL)
    jumlahsetoran = models.IntegerField(null=True)
    harga = models.ForeignKey(Harga, null=True, on_delete=models.SET_NULL)
    tgl = models.DateField(null=True)
    
    def __str__(self):
        return '%s, %s' % (self.nama, self.jumlahsetoran)

