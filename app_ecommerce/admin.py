from django.contrib import admin
from app_ecommerce.models import *
from django.utils.html import format_html
from .models import Like
from app_operaciones.models import Pedido, Categoria, TipoDoc

admin.site.register(Like)

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ("nombre", "apellido", "tipodoc", "nrodoc", "email", "fecha_registro", "fecha_nacimiento", "domicilio")
    list_display_links = ("nombre", "apellido")
    search_fields = ("nrodoc",)
    list_filter = ("fecha_registro", "fecha_nacimiento")
    ordering = ("apellido", "nombre", "nrodoc")
    readonly_fields = ("fecha_registro",)


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "subtitulo", "imagen_preview", "precio", "stock", "categoria", "fecha_publicacion")
    list_display_links = ("nombre", "categoria", "stock")
    search_fields = ("nombre", "subtitulo", "descripcion")
    list_filter = ("nombre", "categoria", "fecha_publicacion")
    ordering = ("nombre", "categoria", "descripcion")

    def imagen_preview(self, obj):
        if obj.imagen:
            try:
                return format_html('<img src="{}" width="50" />', obj.imagen.url)
            except Exception:
                return "-"
        return "-"
    imagen_preview.short_description = "Imagen"


