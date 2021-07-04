from django.urls import path

from . import views

app_name = 'clientes_app'

urlpatterns = [
    path('clientes/', views.ListaClientesView.as_view(), name='clientes'),
    path('api/cliente/list/', views.ClientesListAPIView.as_view()),
    path('api/cliente/create/', views.ClienteCreateView.as_view()),
    path('api/cliente/detail/<pk>/', views.ClienteRetrieveView.as_view()),
    path('api/cliente/destroy/<pk>/', views.ClienteDestroyView.as_view()),
    path('api/cliente/update/<pk>/', views.ClienteUpdateView.as_view()),
]