from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import (
    AuthenticationForm,
    PasswordChangeForm,
)
from django.views.decorators.http import require_POST, require_http_methods
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth import update_session_auth_hash

# Create your views here.


@require_http_methods(["GET", "POST"])
def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('products:market')
    else:
        form = CustomUserCreationForm()
    context = {"form": form}
    return render(request, "accounts/signup.html", context)


@require_http_methods(["GET", "POST"])
def update(request):
    if request.method == "POST":
        form = CustomUserChangeForm(
            request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            username = request.user.username
            return redirect("users:profile", username)
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {"form": form}
    return render(request, "accounts/update.html", context)


def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect("index")
    else:
        form = PasswordChangeForm(request.user)
    context = {"form": form}
    return render(request, "accounts/change_password.html", context)


@require_POST
def delete(request):
    if request.user.is_authenticated:
        request.user.delete()
    return redirect("products:market")


@require_http_methods(["GET", "POST"])
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect("products:market")
    else:
        form = AuthenticationForm()
    context = {
        "form": form
    }
    return render(request, "accounts/login.html", context)


@require_POST
def logout(request):
    if request.method == "POST":
        auth_logout(request)
    return redirect('products:market')
