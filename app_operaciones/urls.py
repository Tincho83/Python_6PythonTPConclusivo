from django.urls import path
from . import views

app_name = 'app_operaciones'

urlpatterns = [
    path('tipodoc/', views.tipodoc_list, name='tipodoc_listar'),
    path('tipodoc/crear/', views.tipodoc, name='tipodoc_crear'),
    path('tipodoc/editar/<int:pk>/', views.tipodoc_editar, name='tipodoc_editar'),
    path('tipodoc/eliminar/<int:pk>/', views.tipodoc_eliminar, name='tipodoc_eliminar'),

    path('categoria/', views.categoria_list, name='categoria_listar'),
    path('categoria/crear/', views.categoria, name='categoria_crear'),
    path('categoria/editar/<int:pk>/', views.categoria_editar, name='categoria_editar'),
    path('categoria/eliminar/<int:pk>/', views.categoria_eliminar, name='categoria_eliminar'),


    path('pedido/', views.pedido_list, name='pedido_listar'),
    path('pedido/crear/', views.pedido, name='pedido_crear'),
    path('pedido/editar/<int:pk>/', views.pedido_editar, name='pedido_editar'),
    path('pedido/eliminar/<int:pk>/', views.pedido_eliminar, name='pedido_eliminar'),
]
