from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('category/', views.category, name='category'),
    path('cart/', views.cart, name='cart'),
    path('product/<slug:slug>/', views.detail, name='product_detail'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('checkout/',views.checkout, name='checkout'),
    path('remove_from_cart/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('update_cart_item/<int:item_id>/', views.update_cart_item, name='update_cart_item'),
    path('checkout/success/<int:order_id>/', views.checkout_success, name='checkout_success'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
