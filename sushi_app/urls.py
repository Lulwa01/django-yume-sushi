from django.urls import path
from . import views

urlpatterns = [
    #routes here
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('orders/', views.order_index, name='orders')
]
