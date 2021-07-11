from rest_framework import serializers

from .models import Order, OrderDetail

class OrderSerializer(serializers.ModelSerializer):

    products = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields =(
            'id',
            'date_order',
            'count' ,
            'amount' ,
            'content' ,
            'close',
            'anulate', 
            'user ',
            'products',
            )
    
    def get_products(self, obj):
        query = OrderDetail.objects.products_by_order(obj.id)
        orders_produced = OrderDetailSerializer(query, many=True)
        return orders_produced

class OrderDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderDetail
        fields = (
           '__all__'
        )