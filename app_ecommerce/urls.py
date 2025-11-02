from django.urls import path
from . import views

app_name = 'app_ecommerce'

urlpatterns = [
    path('', views.index, name='index'),
    path('clientes/registrar/', views.cliente, name='cliente'),        
    path('productos/', views.ProductoListView.as_view(), name='producto_listar'),
    path('productos/nuevo/', views.ProductoCreateView.as_view(), name='producto_crear'),    
    path('productos/<str:cod_prod>/', views.ProductoDetailView.as_view(), name='producto_detalle'),
    path('productos/<str:cod_prod>/editar/', views.ProductoUpdateView.as_view(), name='producto_editar'),
    path('productos/<str:cod_prod>/borrar/', views.ProductoDeleteView.as_view(), name='producto_eliminar'),    
    path('buscar/', views.buscar, name='buscar'),    
    path('productos/<str:cod_prod>/like/', views.producto_like, name='producto_like'),


]
