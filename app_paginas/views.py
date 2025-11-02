from django.shortcuts import render

def about(request):
    return render(request, 'app_paginas/about.html')
