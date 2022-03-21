from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return HttpResponse('<h1>Bienvenido a mi pagina de django</h1>')

def plantilla(request):
    return HttpResponse('')