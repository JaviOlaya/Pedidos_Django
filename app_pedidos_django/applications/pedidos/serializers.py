from rest_framework import serializers,pagination

from .models import Order, OrderDetail

class OrderSerializer(serializers.ModelSerializer):

    products = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields =(
            'id',
            'date_order',  
            'count',
            'amount',
            'content',
            'products', 
            'close',
            'anulate',
            'user_order' ,
    )
    
    def get_products(self, obj):
        query = OrderDetail.objects.products_by_order(obj.id)
        orders_produced = OrderDetailSerializer(query, many=True).data
        return orders_produced

class OrderDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderDetail
        fields = (
            'id',
           'order',
           'product',
           'address_send',
           'count',
           'price_order',
           'anulate',
        )


class ArrayIntegerSerializer(serializers.ListField):

    child = serializers.IntegerField()

class ProductDetailSerializers(serializers.Serializer):
    
    pk = serializers.IntegerField()
    count = serializers.IntegerField()
class ProcessOrderSerializer(serializers.Serializer):

    date = serializers.DateTimeField('Fecha del pedido')
    address_send = serializers.CharField()
    products = ArrayIntegerSerializer()
    amount = ArrayIntegerSerializer()

class PaginationSerializer(pagination.PageNumberPagination):
    
    page_size = 5
    max_page_size = 10

