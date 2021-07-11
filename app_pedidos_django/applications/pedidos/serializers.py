from rest_framework import serializers

from .models import Order

class OrderSerializer(serializers.ModelSerializer):

    products = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields =(
            'date_order',
            'count' ,
            'amount' ,
            'content' ,
            'close',
            'anulate', 
            'user ',
            )
    
    def get_products(self, obj):
        query = OrderDetail.objects.products_by_order()