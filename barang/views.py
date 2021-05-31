from django import forms
from django.shortcuts import render
from barang.models import Akun, Barang
from barang.forms import FormBarang
from django.contrib.auth.decorators import login_required
from django.conf import settings

@login_required(login_url=settings.LOGIN_URL)
def barang(request):
    barang = Barang.objects.all()

    konteks = {
        'barang' : barang
    }
    return render(request, 'adminTambahBarang.html', konteks)

@login_required(login_url=settings.LOGIN_URL)
def akun(request):
    akun = Akun.objects.all()

    konteks = {
        'akun' : akun
    }
    return render(request, 'dataAkun.html', konteks)


def login(request):
    return render(request, 'login.html')

def penerbit(request):
    return render(request, 'penerbit.html')

# Admin Page
# 1. Dashboard Admin
def adminDashboard(request):
    return render(request, 'adminDashboard.html')

# 2. Daftar Akun
def adminAkun(request):
    return render(request, 'adminAkun.html')

# 2.1 Tambah Akun
def adminTambahAkun(request):
    return render(request, 'adminTambahAkun.html')

# 2.2 Edit Akun
def adminEditAkun(request):
    return render(request, 'adminEditAkun.html')

# 3. Daftar Barang
def adminBarang(request):
    return render(request, 'adminBarang.html')

# 3.1 Tambah Barang
def adminTambahBarang(request):
    return render(request, 'adminTambahBarang.html')

def adminTambah_barang(request):
    if request.POST:
        form = FormBarang(request.POST)
        if form.is_valid():
            form.save()
            form = FormBarang()
            pesan = "Data berhasil disimpan"

            konteks = {
                'form' : form,
                'pesan' : pesan,
            }
            return render(request, 'adminTambah_barang', konteks)

    else:
        form = FormBarang()
        pesan = "Data gagal disimpan"

        konteks = {
            'form' : form,
            'pesan': pesan
        }

    return render(request, 'admintambah_barang', konteks)

# 3.2 Edit Barang
def adminEditBarang(request):
    return render(request, 'adminEditBarang.html')


# 4. Daftar Peminjam
def adminPeminjamanDetail(request):
    return render(request, 'adminPeminjamanDetail.html')




# User Page
# 1. User Dashboard
def userDashboard(request):
    return render(request, 'userDashboard.html')

# 2. Akun
def userAkun(request):
    return render(request, 'userAkun.html')

# 3. Barang
def userBarang(request):
    return render(request, 'userBarang.html')
    
# 3.1 Form pinjam barang
def userForm(request):
    return render(request, 'userForm.html')

# 4. Riwayat Peminjaman
def userRiwayat(request):
    return render(request, 'userRiwayat.html')
