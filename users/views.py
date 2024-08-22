from django.shortcuts import (render, redirect, get_object_or_404)
from django.views.decorators.http import require_POST
from django.contrib.auth import get_user_model
from accounts.models import User
from products.models import Product

# Create your views here.


def users(request):
    return render(request, "users/users.html")


def profile(request, username):
    member = get_object_or_404(get_user_model(), username=username)
    followers = member.followers.all().count()
    followings = member.followings.all().count()
    context = {
        "member": member,
        "followers": followers,
        "followings": followings,
    }
    return render(request, "users/profile.html", context)


def my_prdouct(request, username):
    author_id = get_object_or_404(User, username=username).id
    products = Product.objects.filter(author_id=author_id).order_by("-pk")
    context = {
        "username": username,
        "products": products,
    }
    return render(request, "users/my_product.html", context)


@require_POST
def follow(request, user_pk):
    if request.user.is_authenticated:
        member = get_object_or_404(get_user_model(), pk=user_pk)
        if request.user != member:
            if request.user in member.followers.all():
                member.followers.remove(request.user)
            else:
                member.followers.add(request.user)
        return redirect("users:profile", member.username)
    return redirect("accounts:login")
