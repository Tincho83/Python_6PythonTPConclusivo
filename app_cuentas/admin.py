from django.contrib import admin
from .models import Perfil
from django.utils.html import format_html

@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    list_display = ("username", "first_name", "last_name", "tipodoc", "nro_documento", "telefono", "direccion", "avatar_preview")
    search_fields = ('user__username', 'nro_documento')
    readonly_fields = ()

    def avatar_preview(self, obj):
        if obj.avatar:
            return format_html('<img src="{}" width="50" style="object-fit:cover;"/>', obj.avatar.url)
        return "-"
    avatar_preview.short_description = "Avatar"
