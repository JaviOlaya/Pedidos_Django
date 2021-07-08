from django.urls import path


from . import views

app_name = 'pedidos_app'

urlpatterns = [
        path('', include(router.urls)),
    path('api/pedido/list/', views.PedidoListAPIView.as_view()),
    path('api/pedido/create/', views.PedidoCreateView.as_view()),
    path('api/pedido/detail/<pk>/', views.PedidoRetrieveView.as_view()),
    path('api/pedido/destroy/<pk>/', views.PedidoDestroyView.as_view()),
    path('api/pedido/update/<pk>/', views.PedidoUpdateView.as_view()),
]