from django.urls import path

from . import views

app_name = 'clientes_app'

urlpatterns = [
    path('clientes/', views.ListaClientesView.as_view(), name='clientes'),
     path('api/cliente/list/', views.ClientesListAPIView.as_view()),
]