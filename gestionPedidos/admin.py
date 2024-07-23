from django.contrib import admin
from gestionPedidos.models import Cliente,Articulo,Pedido
# Register your models here.

class ClienteAdmin(admin.ModelAdmin):

    list_display = ("nombre","direccion","email","telefono")
    search_fields = ("nombre","telefono")

class ArticuloAdmin(admin.ModelAdmin):

    list_filter = ("seccion",)

class PedidoAdmin(admin.ModelAdmin):

    list_display = ("numero","fecha")
    list_filter = ("fecha",)
    date_hierarchy = "fecha"

admin.site.register(Cliente,ClienteAdmin)
admin.site.register(Articulo,ArticuloAdmin)
admin.site.register(Pedido,PedidoAdmin)
