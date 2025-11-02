from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm, PerfilForm, UserChangeForm
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from .models import Perfil

def registro(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registro exitoso. Ya podés iniciar sesión.")
            return redirect('cuentas:login')
    else:
        form = UserRegisterForm()
    return render(request, 'app_cuentas/registro.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f"Bienvenido, {user.username}!")
            next_url = request.GET.get('next') or '/'
            return redirect(next_url)
    else:
        form = AuthenticationForm()
    return render(request, 'app_cuentas/login.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.info(request, "Has cerrado sesión.")
    return redirect('/')

@login_required
def perfil(request):
    if request.method == 'POST':
        form = PerfilForm(request.POST, request.FILES, instance=request.user.perfil)
        if form.is_valid():
            form.save()
            messages.success(request, "Perfil actualizado.")
            return redirect('cuentas:perfil_ver')
    else:
        form = PerfilForm(instance=request.user.perfil)
    return render(request, 'app_cuentas/perfil.html', {'form': form})

@login_required
def perfil_publico(request, cod_user):
    """Permite ver el perfil de otro usuario usando su cod_user"""
    perfil = get_object_or_404(Perfil, cod_user=cod_user)
    return render(request, 'app_cuentas/perfil_publico.html', {'perfil': perfil})


@login_required
def cambiar_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            # evita cierrre de seiosn
            update_session_auth_hash(request, user)  
            messages.success(request, "Contraseña actualizada correctamente.")
            return redirect('cuentas:perfil_ver')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'app_cuentas/cambiar_password.html', {'form': form})


@login_required
def perfil_ver(request):
    perfil = request.user
    return render(request, 'app_cuentas/perfil_ver.html', {'perfil': perfil})


@login_required
def perfil_editar(request):
    if request.method == 'POST':        
        form = UserChangeForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Perfil actualizado.")
            return redirect('cuentas:perfil_ver')
    else:        
        form = UserChangeForm(instance=request.user)
    return render(request, 'app_cuentas/perfil_editar.html', {'form': form})

