from django.urls import path
from . import views

app_name = 'app_paginas'

urlpatterns = [
    path('about/', views.about, name='about'),
]
