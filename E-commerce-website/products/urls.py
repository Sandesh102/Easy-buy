# products/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'), 
    path('products/',views.products, name='products'),
    path('cart/',views.cart, name='cart'),
    path('detail/',views.detail, name='detao;'),
    
]
