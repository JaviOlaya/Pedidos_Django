from django.urls import path, re_path, include

from . import views

app_name = 'pedidos_app'

urlpatterns = [
    path('api/pedido/list/', views.OrderListAPIView.as_view()),
    path('api/pedido/create/', views.OrderCreateView.as_view()),
    path('api/pedido/detail/<pk>/', views.OrderRetrieveView.as_view()),
    path('api/pedido/destroy/<pk>/', views.OrderDestroyView.as_view()),
    path('api/pedido/update/<pk>/', views.OrderUpdateView.as_view()),
]