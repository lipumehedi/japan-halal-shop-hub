from django.urls import path
from . import views

urlpatterns = [
    path("", views.shop_list, name="shop_list"),
    path("shop/<slug:slug>/", views.shop_detail, name="shop_detail"),
    path("submit-shop/", views.submit_shop, name="submit_shop"),
]
