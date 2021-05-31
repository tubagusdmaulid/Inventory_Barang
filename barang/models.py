from django.db import models
from enum import Enum

class Gedung(models.Model):
    gedung = models.CharField(max_length=10)  
    keterangan = models.TextField()

    def __str__(self):
        return self.gedung

class Ruang(models.Model):
    ruang = models.CharField(max_length=3)
    keterangan = models.TextField()

    def __str__(self):
        return self.ruang


class Barang(models.Model):
    nama_barang = models.CharField(max_length=50)
    merek = models.CharField(max_length=50)
    satuan = models.CharField(max_length=50)
    price = models.CharField(max_length=100)
    stock = models.IntegerField(null=True)
    total_price = models.CharField(max_length=50)
    gedung_id = models.ForeignKey(Gedung, on_delete=models.CASCADE,null=True)
    ruang_id = models.ForeignKey(Ruang, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.nama_barang

# Membuat Tabel akun dan fieldnya
class Akun(models.Model):
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    nama_pegawai = models.CharField(max_length=100)
    nip = models.CharField(max_length=10)
    alamat = models.TextField(max_length=200)
    telepon = models.CharField(max_length=100)

    def __str__(self):
        return self.email

# # Membuat Tabel Peminjaman dan fieldnya
# class Peminjaman(models.Model):
    