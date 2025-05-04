from django import forms
from .models import Side, Order
from .models import INGREDIENTS
from django.forms.widgets import CheckboxSelectMultiple


INGREDIENTS = (
    ('Tuna', 'Tuna'),
    ('Salmon', 'Salmon'),
    ('Crab Stick', 'Crab Stick'),
    ('Shrimp Tempura', 'Shrimp Tempura'),
    ('Eel', 'Eel'),
    ('Avocado', 'Avocado'),
    ('Cucumber', 'Cucumber'),
    ('Cream Cheese', 'Cream Cheese'),
    ('Spicy Mayo', 'Spicy Mayo'),
    ('Wasabi', 'Wasabi'),
    ('Pickled Ginger', 'Pickled Ginger'),
    ('Tamago (Sweet Egg)', 'Tamago (Sweet Egg)'),
    ('Tobiko (Fish Roe)', 'Tobiko (Fish Roe)'),
    ('Sesame Seeds', 'Sesame Seeds'),
    ('Chili Flakes', 'Chili Flakes'),
    ('Spring Onion', 'Spring Onion'),
    ('Carrot', 'Carrot'),
    ('Lettuce', 'Lettuce'),
    ('Radish', 'Radish'),
    ('Seaweed Salad', 'Seaweed Salad'),
    ('Teriyaki Sauce', 'Teriyaki Sauce'),
    ('Soy Sauce', 'Soy Sauce'),
    ('Rice Vinegar', 'Rice Vinegar'),
    ('Sriracha', 'Sriracha'),
)

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'type', 'ingredients', 'price']
        widgets = {
            'type': forms.RadioSelect,
            'ingredients': CheckboxSelectMultiple(),
        }

class SideForm(forms.ModelForm):
    class Meta:
        model = Side
        fields = ['drinks', 'starter']

class Ingredients(forms.ModelForm):
    class Meta:
        choices=INGREDIENTS,
        widget=forms.CheckboxSelectMultiple,    