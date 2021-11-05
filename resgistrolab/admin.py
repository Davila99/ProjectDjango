from django.contrib import admin

from .models import Usuario, Curso, PrestamoLaboratorio, DetallePrestamo

admin.site.register(Usuario)
admin.site.register(Curso)
admin.site.register(PrestamoLaboratorio)
admin.site.register(DetallePrestamo)
# Register your models here.

