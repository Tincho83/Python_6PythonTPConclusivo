from django import forms
from .models import Categoria, TipoDoc, Pedido, DetallePedido
from app_ecommerce.models import Producto
from app_cuentas.models import Perfil

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre', 'descripcion']
        widgets = {
            "nombre" : forms.TextInput(attrs={'class': 'form-control'}),
            "descripcion" : forms.TextInput(attrs={'class': 'form-control'}),
        }

class TipoDocForm(forms.ModelForm):
    class Meta:
        model = TipoDoc
        fields = ['nombre', 'descripcion']
        widgets = {
            "nombre" : forms.TextInput(attrs={'class': 'form-control'}),
            "descripcion" : forms.TextInput(attrs={'class': 'form-control'}),
        }

class PedidoForm(forms.ModelForm):
    producto = forms.ModelMultipleChoiceField(
        queryset=Producto.objects.all(),
        widget=forms.SelectMultiple(attrs={'class': 'form-control'})
    )
    class Meta:
        model = Pedido
        fields = ['cliente', 'producto', 'cantidad']
        widgets = {
            'cliente': forms.Select(attrs={'class': 'form-control'}),            
            'cantidad': forms.NumberInput(attrs={'class': 'form-control', 'min': 1}),
        }
