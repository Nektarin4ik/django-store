from django.contrib import admin

from .models import Product, ProductCategory

# Register your models here.

@admin.register(ProductCategory)
class ProductCategory(admin.ModelAdmin):
    list_display = ['name', 'descrirtion']
    ordering = ['name']
    list_per_page = 10

@admin.register(Product)
class Product(admin.ModelAdmin):
    list_display = ['name', 'description', 'price', 'quantity', 'category']
    ordering = ['price']
    list_per_page = 10
