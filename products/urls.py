from django.urls import path
from . import views

app_name = 'products'
urlpatterns = [
    path("", views.market, name="market"),
    path("new/", views.new, name="new"),
    path("create/", views.create, name="create"),
    path("<int:pk>/", views.detail, name="detail"),
]
