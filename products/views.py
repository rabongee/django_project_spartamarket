from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q, Count
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods, require_POST
from django.contrib import messages
from .models import Product
from .forms import ProductForm


def index(request):
    return render(request, 'index.html')


def market(request):
    order_by = request.GET.get('order_by', '-pk')

    if order_by == '-like_count':
        products = Product.objects.annotate(
            like_count=Count('like_users')
        ).order_by('-like_count', '-pk')
    else:
        products = Product.objects.annotate(
            like_count=Count('like_users')
        ).order_by(order_by)

    for product in products:
        product.hashtags = product.tag_hashtags.all()

    context = {
        "products": products,
    }

    return render(request, 'products/market.html', context)


def detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.views += 1
    product.save()
    like = product.like_users.all()
    hashtags = product.tag_hashtags.all()

    page_from = request.GET.get('ref', 'market')

    context = {
        "product": product,
        "hashtags": hashtags,
        "like": like,
        "page_from": page_from,
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
            return redirect("products:detail", product.pk)
    else:
        form = ProductForm()

    context = {"form": form}
    return render(request, "products/create.html", context)


@login_required
@require_http_methods(["GET", "POST"])
def update(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if product.author != request.user:
        messages.error(request, "남의 게시물은 수정할 수 없습니다!!!")
        return redirect("products:market")

    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            product = form.save(commit=False)
            old_hashtags = product.tag_hashtags.all()
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
        if product.author == request.user:
            product.delete()
            messages.success(request, "게시물이 삭제되었습니다!!!")
        else:
            messages.error(request, "남의 게시물은 삭제할 수 없습니다!!!")
    else:
        messages.error(request, "삭제하려면 로그인하세요!!!")
    return redirect("products:market")


def search(request):
    search_word = request.GET.get("search")

    if not search_word:
        search_products = Product.objects.none()
    else:
        search_products = Product.objects.filter(
            Q(title__icontains=search_word)
            | Q(content__icontains=search_word)
            | Q(author__username__icontains=search_word)
            | Q(tag_hashtags__keyword__icontains=search_word)
        ).order_by("-pk")

    hashtags = []
    if search_products.exists():
        for product in search_products:
            hashtags.extend(product.tag_hashtags.all())

    context = {
        "search_products": search_products,
        "search_word": search_word,
        "hashtags": hashtags,
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
