from rest_framework import serializers, pagination

from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields =(
        'product_name',
        'brand' ,
        'description' ,
        'g_model' ,
        'color_model' ,
        'size_model' ,
        'price' ,
        'stock' ,
        'num_sales', 
        'user_created',
    )


class PaginationSerializer(pagination.PageNumberPagination):

    page_size = 5
    max_page_size = 10

