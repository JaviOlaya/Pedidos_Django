from django.contrib import admin

from .models import Order, OrderDetail
# Register your models here.

class OrderAdmin(admin.ModelAdmin):
    list_display =(
        'date_order', 
        'count', 
        'amount',
        'content',
        'address_send', 
        'order_state',
        'payment_state', 
        'close', 
        'anulate', 
        'user_order',
    )
    search_fields = ('date_order','user_order','amount')
    list_filter = ('user_order','order_state', 'close','anulate')
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderDetail)

