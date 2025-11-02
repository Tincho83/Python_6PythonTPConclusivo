from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from ckeditor.fields import RichTextField
from django.conf import settings
import uuid

def generar_code():
    return uuid.uuid4().hex

class Cliente(models.Model):
    cod_cli = models.CharField(max_length=32, unique=True, default=generar_code)
    nombre = models.CharField(max_length=51)
    apellido = models.CharField(max_length=51)
    tipodoc = models.ForeignKey('app_operaciones.TipoDoc', on_delete=models.CASCADE, related_name="clientes")
    nrodoc = models.IntegerField(unique=True)
    email = models.EmailField()
    fecha_registro = models.DateTimeField(auto_now_add=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    domicilio = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.apellido}, {self.nombre}. {self.tipodoc}: {self.nrodoc}"



class Producto(models.Model):
    cod_prod = models.CharField(max_length=32, unique=True, default=generar_code)
    nombre = models.CharField(max_length=100)
    subtitulo = models.CharField(max_length=150, blank=True)    
    descripcion = RichTextField() 
    imagen = models.ImageField(upload_to='productos/', null=True, blank=True)
    imagen_url = models.URLField(null=True, blank=True)
    precio = models.DecimalField(max_digits=21, decimal_places=2)
    stock = models.PositiveIntegerField()
    categoria = models.ForeignKey('app_operaciones.Categoria', on_delete=models.SET_NULL, null=True, blank=True)    
    fecha_publicacion = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return f"{self.nombre} ({self.cod_prod}) ${self.precio}"

    def clean(self):
        if self.precio <= 0:
            raise ValidationError("El precio debe ser mayor que 0")
        if self.stock < 0:
            raise ValidationError("El stock no puede ser negativo")

    def save(self, *args, **kwargs):
        # Si 'imagen' fue con una URL (string que empiece por http),
        # la guardamos en imagen_url.
        try:
            if isinstance(self.imagen, str) and self.imagen.startswith('http'):
                self.imagen_url = self.imagen
                self.imagen = None
        except Exception:
            pass
        super().save(*args, **kwargs)

    @property
    def imagen_final(self):
        # Prioriza imagen_url (externa), luego imagen (local), sino imsgen estatica
        if self.imagen_url:
            return self.imagen_url
        elif self.imagen:
            try:
                return self.imagen.url
            except ValueError:
                # Por si la imagen no tiene url
                return f"{self.imagen}"
            except Exception:
                return "/static/img/no_image.jpg"
        else:
            return "/static/img/no_image.jpg"



class ContadorVisitas(models.Model):
    total = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"Visitas totales: {self.total}"

class Like(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    producto = models.ForeignKey('Producto', on_delete=models.CASCADE, related_name='likes')
    fecha = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'producto')

    def __str__(self):
        return f"{self.user.username} Le gusta {self.producto.nombre}"