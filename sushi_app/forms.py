from django import forms
from .models import Side
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'type', 'ingredients', 'price']
        widgets = {
            'type': forms.RadioSelect
        }

class SideForm(forms.ModelForm):
    class Meta:
        model = Side
        fields = ['drinks', 'starter']