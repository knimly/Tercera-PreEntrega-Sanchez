from django.contrib import admin
from Registro.models import Cliente, Producto, Entrega 

# Register your models here.
admin.site.register(Cliente)
admin.site.register(Producto)
admin.site.register(Entrega)