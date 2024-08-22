from django.urls import path
from . import views

app_name = 'users'
urlpatterns = [
    path("", views.users, name="users"),
    path("<str:username>/", views.profile, name="profile"),
    path("<str:username>/my_product/", views.my_prdouct, name="my_product"),
    path("<int:user_pk>/follow/", views.follow, name="follow"),
]
