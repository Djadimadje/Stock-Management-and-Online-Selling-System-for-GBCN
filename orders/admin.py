from django.contrib import admin
from .models import Cart, Order

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'order_date', 'status', 'total_amount')
    list_filter = ('status',)
