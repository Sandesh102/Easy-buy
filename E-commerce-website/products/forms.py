from django import forms
from .models import Order

class DeliveryForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['delivery_address', 'phone_number']
