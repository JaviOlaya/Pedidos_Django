from django.shortcuts import render


from django.views.generic import ListView, TemplateView

from rest_framework import viewsets
from rest_framework import status
from rest_framework import generics
from rest_framework.decorators import action
from rest_framework.response import Response
#from rest_framework.generics import ListAPIView, CreateAPIView,RetrieveAPIView, DestroyAPIView, RetrieveUpdateAPIView


# Create your views here.

#Modelo de Producto 
from .models import Product

#serielizers
from .serializers import ProductSerializer, PaginationSerializer

class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    pagination_class = PaginationSerializer
    #queryset = ProductSerializer.Meta.model.objects.filter(state=True)

    # def list(self, request):
    #     product_serializer = self.get_serializer(self.get_queryset(), many = True)
    #     return Response(product_serializer.data, status = status.HTTP_200_OK)


    # def get_queryset(self,pk=None):
    #     if pk is None:
    #         return self.get_serializer().Meta.model.objects.filter(state = True)
    #     return self.get_serializer().Meta.model.objects.filte(id = pk, state = True).first()
    
    # def create(self, request):
    #     serializer = self.serializer_class (data = request.data)
    #     if serializer.is_valid(): 
    #         serializer.save()
    #         return Response({'message': 'El producto se ha creado correctamente!'}, status = status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk = None):
        if self.get_queryset(pk):
            product_serializer = self.serializer_class(self.get_queryset(pk), data = request.data)
            if product_serializer.is_valid():
                product_serializer.save()
                return Response({'message':'El producto se ha actualizado correctamente'},product_serializer.data, status = status.HTTP_200_OK)
            return Response({'error':'No existe un pedido con esos datos'},product_serializer.errors,status = status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk = None):
        product = self.get_queryset().filter(id = pk).first()
        if product:
            product.state = False
            product.save()
            return Response({'message':'Producto eliminado de forma correcta!'}, status = status.HTTP_200_OK)
        return Response({'error': 'No existe un Producto con estos datos!'}, status = status.HTTP_400_BAD_REQUEST)


