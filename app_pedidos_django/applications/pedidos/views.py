from django.shortcuts import render

from rest_framework import status, viewsets,generics
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


#Modelo de Productos
from applications.productos.models import Product
#Modelo de Pedidos
from .models import Order, OrderDetail


#Serializers

from .serializers import OrderSerializer,ProductDetailSerializers,ProcessOrderSerializer,PaginationSerializer

# Create your views here.

class OrderViewSet(viewsets.ViewSet):

    #authentication_classes = (TokenAuthentication,)
    #permission_classes = [IsAuthenticated]
    serializer_class = OrderSerializer
    #pagination_class = PaginationSerializer
    #queryset = Order.objects.all()

    def list(self, request):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def get_queryset(self, pk = None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state = True)
        return self.get_serializer().Meta.model.objects.filter(id = pk, state = True).first()
    
    # def list(self, request):
    #     queryset = Order.objects.all()
    #     serializer = self.get_serializer(self.get_queryset,many = True)
    #     return Response(serializer.data, status=status.HTTP_200_OK)

  
    def create(self, request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'El pedido se ha creado correctamente'},status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk = None):
        if self.get_queryset(pk):
            serializer = self.serializer_class(self.get_queryset(pk),data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message':'El pedido se ha actualizado correctamente'}, serializer.data, status = status.HTTP_200_OK)
            return Response({'error', 'No existe un pedido con estos datos' }, status  = status.HTTP_400_BAD_REQUEST)
            
    def delete(self, request, pk = None):

        order = self.get_queryset().filter(id=pk).first()
        
        if order:
            order.state = False
            order.save()
            return Response({'message':'Pedido eliminado de forma correcta'}, status = status.HTTP_200_OK)
        return Response({'error': 'No existe un pedido con estos datos'}, status = status.HTTP_400_BAD_REQUEST)
        
   


