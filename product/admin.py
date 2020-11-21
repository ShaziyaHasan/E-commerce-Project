from django.contrib import admin
from product.models import Product, Shopping_cart, Order_details


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name','quantity','slug','image','price')


@admin.register(Shopping_cart)
class ShoppingCartAdmin(admin.ModelAdmin):
    pass

@admin.register(Order_details)
class OrderDetailsAdmin(admin.ModelAdmin):
    pass