from django import forms
from django.core.exceptions import ValidationError
from .models import Cliente, Producto
from app_operaciones.models import Pedido, Categoria, TipoDoc
from ckeditor.widgets import CKEditorWidget

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ["nombre", "apellido", "tipodoc", "nrodoc", "email", "fecha_nacimiento", "domicilio"]
        widgets = {
            "nombre" : forms.TextInput(attrs={'class': 'form-control'}),
            "apellido" : forms.TextInput(attrs={'class': 'form-control'}),            
            "tipodoc" :forms.Select(attrs={'class': 'form-control'}),
            "nrodoc" : forms.NumberInput(attrs={'class': 'form-control'}),
            "email" : forms.EmailInput(attrs={'class': 'form-control'}),
            "fecha_nacimiento": forms.DateInput(attrs={'type': 'date', 'class': 'form-control' }),
            "domicilio" : forms.TextInput(attrs={'class': 'form-control'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['tipodoc'].empty_label = "Seleccione un tipo de documento"

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto        
        fields = ["nombre", 'subtitulo', "descripcion", "imagen", "imagen_url", "precio", "stock", "categoria", ]
        widgets = {
            "nombre" : forms.TextInput(attrs={'class': 'form-control'}),
            'subtitulo': forms.TextInput(attrs={'class': 'form-control'}),            
            "descripcion": CKEditorWidget(),            
            "imagen" : forms.ClearableFileInput(attrs={'class': 'form-control'}),
            "imagen_url": forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://... (opcional)'}),
            "precio" : forms.NumberInput(attrs={'class': 'form-control'}),
            "stock" : forms.NumberInput(attrs={'class': 'form-control'}),
            "categoria" : forms.Select(attrs={'class': 'form-control'}),
            'fecha_publicacion': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['categoria'].empty_label = "Seleccione una categoria"

    def clean(self):
        cleaned_data = super().clean()
        precio = cleaned_data.get("precio")
        stock = cleaned_data.get("stock")
        imagen = cleaned_data.get("imagen")
        imagen_url = cleaned_data.get("imagen_url")

        if precio is not None and precio <= 0:
            raise forms.ValidationError("El precio debe ser mayor que cero.")

        if stock is not None and stock < 0:
            raise forms.ValidationError("El stock no puede ser negativo.")

        return cleaned_data


class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['cliente', 'producto', 'cantidad']
        widgets = {
            'cliente': forms.Select(attrs={'class': 'form-select'}),
            'producto': forms.Select(attrs={'class': 'form-select'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control', 'min': 1}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cliente'].empty_label = "Seleccione un cliente"
        self.fields['producto'].empty_label = "Seleccione un producto"



class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ["nombre","descripcion"]
        widgets = {
            "nombre" : forms.TextInput(attrs={'class': 'form-control'}),
            "descripcion" : forms.TextInput(attrs={'class': 'form-control'}),
        }

class TipoDocForm(forms.ModelForm):
    class Meta:
        model = TipoDoc
        fields = ["nombre","descripcion"]
        widgets = {
            "nombre" : forms.TextInput(attrs={'class': 'form-control'}),
            "descripcion" : forms.TextInput(attrs={'class': 'form-control'}),
        }

