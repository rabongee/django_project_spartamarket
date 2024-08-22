from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods, require_POST
from .models import Product
from .forms import ProductForm

def index(request):
    return render(request, 'index.html')



def market(request):
    products = Product.objects.all().order_by("-pk")
    context = {
        "products": products,
    }

    return render(request, 'products/market.html', context)


def detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {"product": product}
    return render(request, "products/detail.html", context)


@login_required
@require_http_methods(["GET", "POST"])
def create(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save()
            return redirect("products:detail", product.pk)
    else:
        form = ProductForm()
        
    context = {"form": form}
    return render(request, "products/create.html", context)


@login_required
@require_http_methods(["GET", "POST"])
def update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            product = form.save()
            return redirect("products:detail", product.pk)
    else:
        form = ProductForm(instance=product)
        
    context = {
        "form": form,
        "product": product,
        }
    return render(request, "products/update.html", context)
    

@require_POST
def delete(request, pk):
    if request.user.is_authenticated:
        product = get_object_or_404(Product, pk=pk)
        product.delete()
    return redirect("products:market")

