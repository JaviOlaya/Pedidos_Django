from django.shortcuts import render

from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, CreateAPIView,RetrieveAPIView, DestroyAPIView, RetrieveUpdateAPIView

#Modelo de Pedidos

from .models import Order, OrderDetail
# Create your views here.

class OrderListAPIView(ListAPIView):
    serializer_class = UsuarioSerializer

    def get_queryset(self):
      
        return Order.objects.all()

class OrderCreateView(CreateAPIView):
    serializer_class = UsuarioSerializer

    def post(self, request):
        serializer = self.serializer_class(data)

class RetrieveView(RetrieveAPIView):
    
    serializer_class = UsuarioSerializer
    queryset = User.objects.all()

class UsuarioDestroyView(DestroyAPIView):
 
    serializer_class = UsuarioSerializer
    queryset = User.objects.all()

class UsuarioUpdateView(RetrieveUpdateAPIView):
    
    serializer_class = UsuarioSerializer
    queryset = User.objects.all()
