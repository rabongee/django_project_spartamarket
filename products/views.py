from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods, require_POST
from django.contrib import messages
from .models import Product
from accounts.models import User
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
    hashtags = product.tag_hashtags.all()
    context = {
        "product": product,
        "hashtags": hashtags,
    }
    return render(request, "products/detail.html", context)


@login_required
@require_http_methods(["GET", "POST"])
def create(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.author = request.user
            product.save()
            hashtags = form.cleaned_data.get('hashtags', [])
            product.add_hashtags(hashtags)
            messages.success(request, "등록이 완료되었습니다!!!  확인해보세요!")
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
            product = form.save(commit=False) 
            old_hashtags = list(product.tag_hashtags.all())
            product.tag_hashtags.clear()
            hashtags = form.cleaned_data.get('hashtags', [])
            product.add_hashtags(hashtags)
            product.save()
            for hashtag in old_hashtags:
                if not hashtag.tag_products.exists():
                    hashtag.delete()
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


def search(request):
    search_word = request.GET.get("search")
    search_products = Product.objects.filter(
        Q(title__icontains=search_word) | Q(content__icontains=search_word) | Q(author__username__icontains=search_word))
    context = {
        "search_products": search_products
    }
    return render(request, 'products/search.html', context)


@require_POST
def like(request, pk):
    if request.user.is_authenticated:
        product = get_object_or_404(Product, pk=pk)
        if product.like_users.filter(pk=request.user.pk).exists():
            product.like_users.remove(request.user)
        else:
            product.like_users.add(request.user)
        return redirect("products:market")
    return redirect("accounts:login")
