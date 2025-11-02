from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import views as auth_views
from . import views

app_name = 'cuentas'

urlpatterns = [
    path('registro/', views.registro, name='registro'),    
    path('login/', LoginView.as_view(template_name="app_cuentas/login.html"), name='login'),    
    path('logout/', LogoutView.as_view(template_name="app_cuentas/logout.html"), name='logout'),    
    path('perfil/', views.perfil_ver, name='perfil_ver'),
    path('perfil/editar/', views.perfil_editar, name='perfil_editar'),    
    path('perfil/cambiar-password/', views.cambiar_password, name='cambiar_password'),    
    path('perfil/<str:cod_user>/', views.perfil_publico, name='perfil_publico'),

]
