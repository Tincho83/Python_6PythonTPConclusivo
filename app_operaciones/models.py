from django.db import models
import uuid

def generar_code():
    return uuid.uuid4().hex

class TipoDoc(models.Model):
    nombre = models.CharField(max_length=7, unique=True)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre



class Categoria(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre

class Pedido(models.Model):
    cod_ped = models.CharField(max_length=32, unique=True, default=generar_code)
    cliente = models.ForeignKey('app_cuentas.Perfil', on_delete=models.CASCADE)
    producto = models.ManyToManyField('app_ecommerce.Producto', through='DetallePedido')
    cantidad = models.PositiveIntegerField(default=1)
    fecha_pedido = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=21, decimal_places=2, default=0)

    def calcular_total(self):
        return sum(det.subtotal for det in self.detallepedido_set.all())
    
    def save(self, *args, **kwargs):
        # calcular total automáticamente si hay producto y cantidad
        try:
            self.total = self.calcular_total()
        except Exception:
            self.total = 0
        super().save(*args, **kwargs)
        
    def __str__(self):
        return f"Pedido #{self.cod_ped} - {self.cliente}"

    
class DetallePedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    producto = models.ForeignKey('app_ecommerce.Producto', on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)
    subtotal = models.DecimalField(max_digits=21, decimal_places=2)

    def __str__(self):
        return f"{self.producto} x {self.cantidad}"

