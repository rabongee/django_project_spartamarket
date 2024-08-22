from django.shortcuts import render
from .models import Product


def index(request):
    return render(request, 'index.html')


def market(request):
    products = Product.objects.all()
    context = {
        "products": products,
    }
    return render(request, 'products/market.html', context)