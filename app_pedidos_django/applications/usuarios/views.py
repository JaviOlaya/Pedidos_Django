from django.shortcuts import render


from django.views.generic import ListView, TemplateView

from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, CreateAPIView,RetrieveAPIView, DestroyAPIView, RetrieveUpdateAPIView


# Create your views here.

#Modelo de Usuario 
from .models import Usuario

#serielizers
from .serializers import UsuarioSerializer,UsuarioLoginSerializer

class USerViewSet(viewsets.GenericViewSet):

    queryset = Usuario.objects
    serielizer_class = UsuarioSerializer

    @action(detail = False, methods=['POST'])
    def login(self, request):
        
        serializer = UsuarioLoginSerializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        user, token = serializer.save()
        data = {
            'user': UsuarioLoginSerializer(user).data,
            'access_token': token
        }

        return Response(data, status=status.HTTP_201_CREATED)

        
class UsuarioListAPIView(ListAPIView):
    serializer_class = UsuarioSerializer

    def get_queryset(self):
      
        return Usuario.objects.all()

class UsuarioCreateView(CreateAPIView):
    serializer_class = UsuarioSerializer

    def post(self, request):
        serializer = self.serializer_class(data)

class UsuarioRetrieveView(RetrieveAPIView):
    
    serializer_class = UsuarioSerializer
    queryset = Usuario.objects.all()

class UsuarioDestroyView(DestroyAPIView):
 
    serializer_class = UsuarioSerializer
    queryset = Usuario.objects.all()

class UsuarioUpdateView(RetrieveUpdateAPIView):
    
    serializer_class = UsuarioSerializer
    queryset = Usuario.objects.all()