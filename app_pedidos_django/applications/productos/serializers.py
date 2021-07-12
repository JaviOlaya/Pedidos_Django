from rest_framework import serializers, pagination

from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields =('__all__')

class PaginationSerializer(pagination.PageNumberPagination):

    page_size = 5
    max_page_size = 10

