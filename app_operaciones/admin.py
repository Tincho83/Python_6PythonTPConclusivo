from django.contrib import admin
from .models import Pedido, TipoDoc, Categoria 

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ("cliente", "listar_productos", "cantidad", "fecha_pedido")
    list_display_links = ("cliente", "listar_productos", "fecha_pedido")
    search_fields = ("cliente",)    
    list_filter = ("cliente", "fecha_pedido")
    ordering = ("cliente", "fecha_pedido")
    readonly_fields = ("fecha_pedido",)

    def listar_productos(self, obj):
        return ", ".join([p.nombre for p in obj.producto.all()])
    listar_productos.short_description = "Productos"

@admin.register(TipoDoc)
class TipoDocAdmin(admin.ModelAdmin):
    list_display = ("nombre", "descripcion")
    list_display_links = ("nombre", "descripcion")
    search_fields = ("nombre",)
    list_filter = ("nombre", "descripcion")
    ordering = ("nombre", "descripcion")

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "descripcion")
    list_display_links = ("nombre", "descripcion")
    search_fields = ("nombre",)
    list_filter = ("nombre", "descripcion")
    ordering = ("nombre", "descripcion")
