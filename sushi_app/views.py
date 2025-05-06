from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from .models import Order, Side
from .forms import SideForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse


# Create your views here.

class Home(LoginView):
    template_name = 'home.html'


@login_required
def order_index(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'orders/index.html', {'orders': orders})

def order_detail(request, order_id):
    order = Order.objects.get(id=order_id)
    side_form = SideForm()
    return render(request, 'orders/detail.html', {
        'order': order, 
        'side_form': side_form
    })

class SushiCreate(LoginRequiredMixin, CreateView):
    model = Order
    fields = ['name', 'type', 'ingredients', 'price']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class SushiUpdate(UpdateView):
    model = Order
    fields = ['name', 'type', 'ingredients', 'price']

class SushiDelete(DeleteView):
    model = Order
    success_url = '/orders/'
    template_name = 'sushi_app/order_confirm_delete.html'

def add_side(request, order_id):
    order = Order.objects.get(id=order_id)

    if hasattr(order, 'side'):
        return redirect('order-detail', order_id=order_id)
    
    form = SideForm(request.POST)
    if form.is_valid():
        new_side = form.save(commit=False)
        new_side.order_id = order_id
        new_side.save()
    return redirect('order-detail', order_id=order_id)

class SideUpdate(UpdateView):
    model = Side
    form_class = SideForm
    template_name = 'sides/side_form.html'

    def get_success_url(self):
        return reverse('order-detail', kwargs={'order_id': self.object.order.id})


def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('order-index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)