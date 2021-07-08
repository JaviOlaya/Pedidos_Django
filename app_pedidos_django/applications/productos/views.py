from django.shortcuts import render


from django.views.generic import ListView, TemplateView

from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, CreateAPIView,RetrieveAPIView, DestroyAPIView, RetrieveUpdateAPIView


# Create your views here.

#Modelo de Producto 
from .models import Product

#serielizers
from .serializers import ProductSerializer




class ProductListAPIView(ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
      
        return Product.objects.all()

class ProductCreateView(CreateAPIView):
    serializer_class = ProductSerializer

    def post(self, request):
        serializer = self.serializer_class(data)

class ProductRetrieveView(RetrieveAPIView):
    
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

class ProductDestroyView(DestroyAPIView):
 
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

class ProductUpdateView(RetrieveUpdateAPIView):
    
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
