from django.shortcuts import render


from django.views.generic import ListView, TemplateView

from rest_framework import viewsets
from rest_framework import status
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
#from rest_framework.generics import ListAPIView, CreateAPIView,RetrieveAPIView, DestroyAPIView, RetrieveUpdateAPIView


# Create your views here.

#Modelo de Producto 
from .models import Product

#serielizers
from .serializers import ProductSerializer, PaginationSerializer

class ListProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    

    def create(self, request):
        serializer = self.serializer_class (data = request.data)
        if serializer.is_valid(): 
            serializer.save()
            return Response({'message': 'El producto se ha creado correctamente!'}, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

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


    pagination_class = PaginationSerializer

class ListProductUserViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    #queryset = Product.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated]
    #queryset = ProductSerializer.Meta.model.objects.filter(state=True)

    # def list(self, request):
    #     product_serializer = self.get_serializer(self.get_queryset(), many = True)
    #     return Response(product_serializer.data, status = status.HTTP_200_OK)

    def get_queryset(self,pk=None):
        usuario = self.request.user
        print(usuario)
        return Product.objects.productos_por_user(usuario)
        
    pagination_class = PaginationSerializer
#     def create(self, request):
#         serializer = self.serializer_class (data = request.data)
#         if serializer.is_valid(): 
#             serializer.save()
#             return Response({'message': 'El producto se ha creado correctamente!'}, status = status.HTTP_201_CREATED)
#         return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

#     def update(self, request, pk = None):
#         if self.get_queryset(pk):
#             product_serializer = self.serializer_class(self.get_queryset(pk), data = request.data)
#             if product_serializer.is_valid():
#                 product_serializer.save()
#                 return Response({'message':'El producto se ha actualizado correctamente'},product_serializer.data, status = status.HTTP_200_OK)
#             return Response({'error':'No existe un pedido con esos datos'},product_serializer.errors,status = status.HTTP_400_BAD_REQUEST)


#     def delete(self, request, pk = None):
#         product = self.get_queryset().filter(id = pk).first()
#         if product:
#             product.state = False
#             product.save()
#             return Response({'message':'Producto eliminado de forma correcta!'}, status = status.HTTP_200_OK)
#         return Response({'error': 'No existe un Producto con estos datos!'}, status = status.HTTP_400_BAD_REQUEST)

#     pagination_class = PaginationSerializer
# class ListProductStock(viewsets.ModelViewSet):
#     serializer_class = ProductSerializer
#     #authentication_classes = (TokenAuthentication,)
#     #permission_classes = [IsAuthenticated, IsAdminUser]

#     def get_queryset(self):

#         return Product.objects.productos_stock()