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


def detail(request, pk):
    product = Product.objects.get(pk=pk)
    context = {"product": product}
    return render(request, "products/detail.html", context)


def new(request):
    return render(request, "products/new.html")


def create(request):
    title = request.POST.get("title")
    content = request.POST.get("content")
    price = request.POST.get("price")
    product = Product.objects.create(title=title, content=content, price=price)
    return redirect("products:detail", product.pk)


def edit(request, pk):
    product = Product.objects.get(pk=pk)
    context = {"product": product}
    return render(request, "products/edit.html", context)


def update(request, pk):
    title = request.POST.get("title")
    content = request.POST.get("content")
    price = request.POST.get("price")
    product = Product.objects.get(pk=pk)
    product.title = title
    product.content = content
    product.price = price
    product.save()
    return redirect("products:detail", product.pk)


def delete(request, pk):
    if request.method == "POST":
        product = Product.objects.get(pk=pk)
        product.delete()
        return redirect("products:market")
    return redirect("products:detail", pk)