from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from .models import Order
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.

def home(request):
    return render(request, 'home.html')

# class Orders:
#     def __init__(self, name, type, ingredient, price):
#         self.name = name
#         self.type = type
#         self.ingredients = ingredient
#         self.price = price

# orders = [
#     Orders('Dragon Roll', 'Maki', ['Shrimp Tempura', 'Avocado', 'Eel Sauce'], 12.99),
#     Orders('Salmon Nigiri', 'Nigiri', ['Salmon', 'Sushi Rice'], 5.99),
#     Orders('Spicy Tuna Roll', 'Maki', ['Tuna', 'Spicy Mayo', 'Cucumber'], 8.49),
#     Orders('California Roll', 'Maki', ['Crab', 'Avocado', 'Cucumber'], 7.99),
#     Orders('Vegetarian Roll', 'Maki', ['Avocado', 'Cucumber', 'Carrot'], 6.50)
# ]

def order_index(request):
    orders = Order.objects.all()
    return render(request, 'orders/index.html', {'orders': orders})

def order_detail(request, order_id):
    order = Order.objects.get(id=order_id)
    return render(request, 'orders/detail.html', {'order': order})

class SushiCreate(CreateView):
    model = Order
    fields = '__all__'

class SushiUpdate(UpdateView):
    model = Order
    fields = '__all__'

class SushiDelete(DeleteView):
    model = Order
    success_url = '/orders/'
