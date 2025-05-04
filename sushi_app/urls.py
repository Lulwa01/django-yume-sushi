from django.urls import path
from . import views

urlpatterns = [
    #routes here
    path('', views.Home.as_view(), name='home'),
    path('orders/', views.order_index, name='order-index'),
    path('orders/<int:order_id>/', views.order_detail, name='order-detail'),
    path('orders/new', views.SushiCreate.as_view(), name='order-create'),
    path('orders/<int:pk>/update/', views.SushiUpdate.as_view(), name='order-update'),
    path('orders/<int:pk>/delete/', views.SushiDelete.as_view(), name='order-delete'),
    path('orders/<int:order_id>/add-side/', views.add_side, name='add-side'),
    path('accounts/signup/', views.signup, name='signup'),
    path('sides/<int:pk>/edit/', views.SideUpdate.as_view(), name='side-update'),
]