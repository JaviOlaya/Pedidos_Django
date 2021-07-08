from django.shortcuts import render

from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, CreateAPIView,RetrieveAPIView, DestroyAPIView, RetrieveUpdateAPIView

#Modelo de Pedidos

from .models import Order, OrderDetail

#Serializers

from .serializer import OrderSerializer

# Create your views here.

class OrderListAPIView(ListAPIView):
    serializer_class = OrderSerializer

    def get_queryset(self):
      
        return Order.objects.all()

class OrderCreateView(CreateAPIView):
    serializer_class = OrderSerializer

    def post(self, request):
        serializer = self.serializer_class(data)

class OrderRetrieveView(RetrieveAPIView):
    
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

class OrderDestroyView(DestroyAPIView):
 
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

class OrderUpdateView(RetrieveUpdateAPIView):
    
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
