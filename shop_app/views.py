from django.shortcuts import render, redirect
from .models import *

# Create your views here.


def index(request):
    return render(request, 'shop_main.html')


def cart(request):
    return render(request, 'shop_cart.html')
