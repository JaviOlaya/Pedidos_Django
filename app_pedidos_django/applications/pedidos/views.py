from django.shortcuts import render

from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response


#Modelo de Pedidos

from .models import Order, OrderDetail

#Serializers

from .serializers import OrderSerializer

# Create your views here.

class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state = True)
        return self.get_serializer().Meta.model.objects.filter(id = pk,state = True).first()
    
    def list(self, request):
        product_serializer = self.get_serializer(self.get_queryset(),many = True)
        return Response(product_serializer.data, status=status.HTTP_200_OK)
    
    def create(self, request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'El pedido se ha creado correctamente'},status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk = None):
        if self.get_queryset(pk):
            product_serializer = self.serializer_class(self.get_queryset(pk),data = request.data)
            if product_serializer.is_valid():
                product_serializer.save()
                return Response({'message':'El pedido se ha actualizado correctamente'},product_serializer.data, status = status.HTTP_200_OK)
            return Response({'error', 'No existe un pedido con estos datos' }, status  = status.HTTP_400_BAD_REQUEST)
            
    def delete(self, request, pk = None):

        order = self.get_queryset().filter(id=pk).first()
        
        if order:
            order.state = False
            order.save()
            return Response({'message':'Pedido eliminado de forma correcta'}, status = status.HTTP_200_OK)
        return Response({'error': 'No existe un pedido con estos datos'}, status = status.HTTP_400_BAD_REQUEST)
        



