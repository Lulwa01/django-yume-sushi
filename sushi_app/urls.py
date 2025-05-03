from django.urls import path
from . import views

urlpatterns = [
    #routes here
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('orders/', views.order_index, name='order-index'),
    path('orders/<int:order_id>/', views.order_detail, name='order-detail'),
    path('orders/new', views.SushiCreate.as_view(), name='order-create'),
    path('orders/<int:pk>/update/', views.SushiUpdate.as_view(), name='order-update'),
    path('orders/<int:pk>/delete/', views.SushiDelete.as_view(), name='order-delete'),
]