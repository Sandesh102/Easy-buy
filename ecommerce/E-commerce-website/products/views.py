

from django.shortcuts import render

def homepage(request):
    return render(request, 'products/home.html')  
def products(request):
    return render(request, 'products/products.html')
def cart(request):
    return render(request,'products/cart.html')
def detail(request):
    return render(request,'products/detail.html')
