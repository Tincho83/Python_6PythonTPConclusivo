from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from app_operaciones.models import TipoDoc
from .models import Perfil

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control'}))    

    class Meta:        
        model = Perfil        
        fields = ["username", "email", "first_name", "last_name", "password1", "password2"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # clases
        for field in self.fields:
            if not isinstance(self.fields[field].widget, (forms.PasswordInput,)):
                self.fields[field].widget.attrs.update({'class': 'form-control'})
        # campos pra la contrasenia
        self.fields['password1'].widget.attrs.update({'class': 'form-control'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control'})


    def save(self, commit=True):
        user = super().save(commit)
        # Crear el perfil con los nuevos campos        
        return user

class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['first_name', 'last_name', 'tipodoc', 'nro_documento', 'telefono', 'direccion', 'avatar', 'bio', 'fecha_nacimiento', 'link', 'pais']
        widgets = {
            'first_name': forms.TextInput(attrs={'class':'form-control'}),
            'last_name': forms.TextInput(attrs={'class':'form-control'}),
            'tipodoc': forms.Select(attrs={'class': 'form-control'}),
            'nro_documento': forms.NumberInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class':'form-control'}),
            'direccion': forms.TextInput(attrs={'class':'form-control'}),
            'avatar': forms.ClearableFileInput(attrs={'class':'form-control'}),
            'bio': forms.Textarea(attrs={'class':'form-control', 'rows':3}),
            'fecha_nacimiento': forms.DateInput(attrs={'class':'form-control', 'type':'date'}, format='%Y-%m-%d'),
            'link': forms.URLInput(attrs={'class':'form-control'}),
            'pais': forms.TextInput(attrs={'class':'form-control'}),
        }


class UserChangeForm(UserChangeForm):
    password = None
    class Meta:
        model = Perfil
        exclude = ("cod_user", "password")
        fields = ['first_name', 'last_name', 'tipodoc', 'nro_documento', 'telefono', 'direccion', 'avatar', 'bio', 'fecha_nacimiento', 'link', 'pais']
        widgets = {
            'first_name': forms.TextInput(attrs={'class':'form-control'}),
            'last_name': forms.TextInput(attrs={'class':'form-control'}),
            'tipodoc': forms.Select(attrs={'class': 'form-control'}),
            'nro_documento': forms.NumberInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class':'form-control'}),
            'direccion': forms.TextInput(attrs={'class':'form-control'}),
            'avatar': forms.ClearableFileInput(attrs={'class':'form-control'}),
            'bio': forms.Textarea(attrs={'class':'form-control', 'rows':3}),
            'fecha_nacimiento': forms.DateInput(attrs={'class':'form-control', 'type':'date'}, format='%Y-%m-%d'),
            'link': forms.URLInput(attrs={'class':'form-control'}),
            'pais': forms.TextInput(attrs={'class':'form-control'}),
        }
