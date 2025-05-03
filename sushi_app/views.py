from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from .models import Order, Side
from .forms import SideForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect

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
    side_form = SideForm()
    return render(request, 'orders/detail.html', {
        'order': order, 
        'side_form': side_form
    })

class SushiCreate(CreateView):
    model = Order
    fields = '__all__'

class SushiUpdate(UpdateView):
    model = Order
    fields = '__all__'

class SushiDelete(DeleteView):
    model = Order
    success_url = '/orders/'
    template_name = 'sushi_app/order_confirm_delete.html'

def add_side(request, order_id):
    form = SideForm(request.POST)
    if form.is_valid():
        new_side = form.save(commit=False)
        new_side.order_id = order_id
        new_side.save()
    return redirect('order-detail', order_id=order_id)