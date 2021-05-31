from django.contrib import admin
from django.urls import path
from perpustakaan.views import *
from django.contrib.auth.views import LoginView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('buku/', buku),
    path('penerbit/', penerbit),

    path('akun/', akun),

    path('login/', login),
    path('masuk/', LoginView.as_view, name='masuk'),

    # Admin Page
    # 1. Dashboard
    path('adminDashboard/', adminDashboard),

    # 2. Akun
    path('adminAkun/', adminAkun),
    # 2.1 Tambah Akun
    path('adminTambahAkun/', adminTambahAkun),
    # 2.2 Edit Akun
    path('adminEditAkun/', adminEditAkun),

    # 3. Barang
    path('adminBarang/', adminBarang),
    # 3.1 Tambah Barang
    path('adminTambah_barang/', adminTambah_barang),
    path('adminTambahBarang/', adminTambahBarang),
    # 3.2 Edit Barang
    path('adminEditBarang/', adminEditBarang),

    # 4. Peminjaman Detail
    path('adminPeminjamanDetail/', adminPeminjamanDetail),


    # User Page
    # 1. Dashboard
    path('userDashboard/', userDashboard),

    # 2. Akun
    path('userAkun/', userAkun),

    # 3.Barang
    path('userBarang/', userBarang),
    # 3.1 Form Pinjam Barang
    path('userForm/', userForm),

    # 4. Riwayat Peminjaman
    path('userRiwayat/', userRiwayat),
]
