from django.contrib import admin
from .models import Product
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display=(
    'product_name',
    'brand',
    'description',
    'g_model',
    'color_model',
    'size_model',
    'price', 
    'stock', 
    'num_sales',
    'user_created',
    )
    search_fields = ('product_name','g_model','user_created')
    list_filter = ('g_model','color_model', 'stock')
admin.site.register(Product, ProductAdmin)
