from django.shortcuts import render, redirect
from .models import Product


def index(request):
    return render(request, 'index.html')


def market(request):
    products = Product.objects.all().order_by("-pk")
    context = {
        "products": products,
    }
    return render(request, 'products/market.html', context)


def new(request):
    return render(request, "products/new.html")


def create(request):
    title = request.POST.get("title")
    content = request.POST.get("content")
    price = request.POST.get("price")
    Product.objects.create(title=title, content=content, price=price)
    return redirect("products:market")