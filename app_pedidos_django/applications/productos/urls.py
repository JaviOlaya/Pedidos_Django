from django.urls import path


from . import views

app_name = 'productos_app'

urlpatterns = [
        path('', include(router.urls)),
    path('api/producto/list/', views.ProductoListAPIView.as_view()),
    path('api/producto/create/', views.ProductoCreateView.as_view()),
    path('api/producto/detail/<pk>/', views.ProductoRetrieveView.as_view()),
    path('api/producto/destroy/<pk>/', views.ProductoDestroyView.as_view()),
    path('api/producto/update/<pk>/', views.ProductoUpdateView.as_view()),
]