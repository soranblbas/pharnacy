from django.shortcuts import render
from .models import *


def home(request):
    return render(request, 'home.html')


def products(request):
    return render(request, 'products.html')


def contact(request):
    return render(request, 'contact.html')


def about(request):
    return render(request, 'about.html')