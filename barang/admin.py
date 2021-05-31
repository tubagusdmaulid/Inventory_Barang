from django.contrib import admin
from perpustakaan.models import Akun, Barang, Gedung, Ruang

# Register your models here.
class BarangAdmin(admin.ModelAdmin):
    list_display = ['nama_barang', 'gedung_id', 'ruang_id', 'stock', 'price']
    search_fields = ['nama_barang', 'gedung_id','ruang_id']
    list_filter = ('gedung_id', 'ruang_id')
    list_per_page = 2


admin.site.register(Barang, BarangAdmin)
admin.site.register(Gedung)
admin.site.register(Ruang)
admin.site.register(Akun)
