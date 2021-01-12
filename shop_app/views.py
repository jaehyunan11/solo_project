from django.shortcuts import render, redirect

# Create your views here.


def index(request):
    return render(request, 'shop_main.html')


def cart(request):
    return render(request, 'shop_cart.html')
