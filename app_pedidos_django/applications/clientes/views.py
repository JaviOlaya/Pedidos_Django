from django.shortcuts import render

from .models import Cliente

from django.views.generic import ListView

from rest_framework.generics import ListAPIView

# Create your views here.

from .models import Cliente

from .serializers import ClienteSerializer

class ListaClientesView(ListView):
    template_name = "clientes/clientes.html"
    context_object_name = 'clientes'

    def get_queryset(self):
        return Cliente.objects.all()


class ClientesListAPIView(ListAPIView):
    serializer_class = ClienteSerializer

    def get_queryset(self):
      
        return Cliente.objects.all()