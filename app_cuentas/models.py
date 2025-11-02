from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.dispatch import receiver
from django.db.models.signals import post_save
import uuid


def avatar_upload_to(instance, filename):
    return f"avatars/{instance.username}/{filename}"

def generar_code(): 
    return uuid.uuid4().hex

class Perfil(AbstractUser):
    cod_user = models.CharField(max_length=32, unique=True, default=generar_code)
    telefono = models.CharField(max_length=20, blank=True)
    direccion = models.CharField(max_length=255, blank=True)    
    #avatar = models.ImageField(upload_to=avatar_upload_to, null=True, blank=True, default='avatars/perfil_default.jpg')
    avatar = models.ImageField(upload_to=avatar_upload_to, null=True, blank=True)
    bio = models.CharField(max_length=512, blank=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    link = models.URLField(null=True, blank=True)
    pais = models.CharField(max_length=51, blank=True)
    tipodoc = models.ForeignKey('app_operaciones.TipoDoc', on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Tipo de Documento")
    nro_documento = models.PositiveIntegerField(unique=True, null=True, blank=True, verbose_name="Número de Documento")

    @property
    def avatar_url(self):
        """Devuelve la URL del avatar o la imagen estática por defecto."""
        if self.avatar:
            return self.avatar.url
        return '/static/perfil_default.jpg'

    def __str__(self):
        return f"Perfil de {self.username}: {self.last_name}, {self.first_name}"
