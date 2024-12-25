

from django.shortcuts import render
from .models import Product
def homepage(request):
    products= Product.objects.all()  
    return render(request,'products/home.html', {'products': products})  
def products(request):
    return render(request, 'products/products.html')
def cart(request):
    return render(request,'products/cart.html')
def detail(request):
    return render(request,'products/detail.html')
    
def category(request):
    return render(request,'products/category.html')

