from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def habitaciones(request):
    return render(request,'habitaciones.html')

def usuario(request):
    return render(request,'usuario.html')

def perfiles(request):
    return render(request,'perfiles.html')

def registro(request):
    return render(request,'registro.html')