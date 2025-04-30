from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'home.html')

class Orders:
    def __init__(self, name, type, ingredient, price):
        self.name = name
        self.type = type
        self.ingredients = ingredient
        self.price = price

orders = [
    Orders('Dragon Roll', 'Maki', ['Shrimp Tempura', 'Avocado', 'Eel Sauce'], 12.99),
    Orders('Salmon Nigiri', 'Nigiri', ['Salmon', 'Sushi Rice'], 5.99),
    Orders('Spicy Tuna Roll', 'Maki', ['Tuna', 'Spicy Mayo', 'Cucumber'], 8.49),
    Orders('California Roll', 'Maki', ['Crab', 'Avocado', 'Cucumber'], 7.99),
    Orders('Vegetarian Roll', 'Maki', ['Avocado', 'Cucumber', 'Carrot'], 6.50)
]

def order_index(request):
    return render(request, 'orders/index.html', {'orders': orders})