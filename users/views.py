from django.shortcuts import render
from django.shortcuts import get_object_or_404
from accounts.models import User

# Create your views here.


def users(request):
    return render(request, "users/users.html")


def profile(request, username):
    user = get_object_or_404(User, username=username)
    context = {
        "user": user
    }
    return render(request, "users/profile.html", context)
