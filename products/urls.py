from django.urls import path
from . import views

app_name = 'products'
urlpatterns = [
    path("", views.market, name="market"),
    path("create/", views.create, name="create"),
    path("<int:pk>/", views.detail, name="detail"),
    path("<int:pk>/delete/", views.delete, name="delete"),
    path("<int:pk>/update/", views.update, name="update"),
    path("search/", views.search, name='search'),
    path("<int:pk>/like/", views.like, name="like"),
]
