from django.contrib import admin
from .models import Order, Side
# Register your models here.

admin.site.register(Order) 
admin.site.register(Side)