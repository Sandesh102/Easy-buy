from products.models import Category, Product,CartItem
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.conf import settings
import qrcode
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

from .forms import *
# @login_required(login_url='login')
def homepage(request):
    products= Product.objects.all()  
    return render(request,'products/home.html', {'products': products})  
def products(request):
    return render(request, 'products/products.html')
@login_required(login_url='login')
def cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    
    context = {
        'cart_items': cart_items,
        'total_price': total_price,
    }
    return render(request, 'products/cart.html', context)

def detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'products/detail.html', {'product': product})
    
def category(request):
    categories = Category.objects.all()  # Get all categories

    # Filter products based on category and price range
    products = Product.objects.all()

    # Filter by category if selected
    category_id = request.GET.get('category')
    if category_id:
        products = products.filter(category_id=category_id)

    # Filter by min price if provided
    min_price = request.GET.get('min_price')
    if min_price:
        products = products.filter(price__gte=min_price)

    # Filter by max price if provided
    max_price = request.GET.get('max_price')
    if max_price:
        products = products.filter(price__lte=max_price)

    # Pass the filtered products and categories to the template
    return render(request, 'products/category.html', {
        'categories': categories,
        'products': products
    })

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    
    # Get the quantity from the POST request and set a default of 1 if not provided
    quantity = request.POST.get('quantity')
    
    if not quantity or int(quantity) <= 0:
        quantity = 1  # Default to 1 if quantity is invalid or missing

    # Ensure quantity is treated as an integer
    quantity = int(quantity)

    # Retrieve the cart item or create a new one
    cart_item, created = CartItem.objects.get_or_create(user=request.user, product=product)

    if not created:
        # If the cart item already exists, update the quantity
        cart_item.quantity += quantity
        cart_item.save()
    else:
        # If the cart item is new, set the quantity
        cart_item.quantity = quantity
        cart_item.save()

    return redirect('cart')  # Redirect to the cart page



from django.core.files.storage import FileSystemStorage

@login_required(login_url='login')
def checkout(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    qr_code_path = f"{settings.MEDIA_URL}qr_codes/order_payment_qr.png"  # Update this to your static QR path

    if request.method == "POST":
        form = DeliveryForm(request.POST, request.FILES)  # Include request.FILES for file uploads
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.total_price = total_price
            order.payment_proof = request.FILES.get('payment_proof')  # Save the uploaded file
            order.save()

            # Clear the cart after checkout
            cart_items.delete()

            return render(request, 'products/checkout_success.html', {'order': order, 'qr_code_path': qr_code_path})
    else:
        form = DeliveryForm()

    context = {
        'form': form,
        'cart_items': cart_items,
        'total_price': total_price,
        'qr_code_path': qr_code_path,
    }
    return render(request, 'products/checkout.html', context)



@login_required
def remove_from_cart(request, item_id):
    item = get_object_or_404(CartItem, id=item_id, user=request.user)
    item.delete()
    return redirect('cart')

def cart(request):
    # Get the cart items for the logged-in user
    cart_items = CartItem.objects.filter(user=request.user)

    # Calculate the total price
    total_price = sum(item.product.price * item.quantity for item in cart_items)

    return render(request, 'products/cart.html', {'cart_items': cart_items, 'total_price': total_price})

def update_cart_item(request, item_id):
    item = get_object_or_404(CartItem, id=item_id, user=request.user)
    if request.method == "POST":
        action = request.POST.get('action')
        if action == "increase":
            item.quantity += 1
        elif action == "decrease" and item.quantity > 1:
            item.quantity -= 1
        item.save()
    return redirect('cart')  # Redirect back to the cart page

@login_required(login_url='login')
def checkout_success(request, order_id):
    try:
        # Retrieve the completed order
        order = Order.objects.get(id=order_id, user=request.user)
    except Order.DoesNotExist:
        # Redirect to the cart or an error page if the order does not exist
        messages.error(request, "Order not found.")
        return redirect('cart')  # Replace 'cart' with the appropriate URL name

    context = {
        'order': order,
        'qr_code_path': f"{settings.MEDIA_URL}qr_codes/order_{order.id}.png",  # Update to your QR code path
    }
    return render(request, 'products/checkout_success.html', context)
