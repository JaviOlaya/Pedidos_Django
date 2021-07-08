from django.urls import path


from . import views

app_name = 'productos_app'

urlpatterns = [
    path('api/producto/list/', views.ProductListAPIView.as_view(), name='product_list'),
    path('api/producto/create/', views.ProductCreateView.as_view(),name='new_product'),
    path('api/producto/detail/<pk>/', views.ProductRetrieveView.as_view(),name='detail_product'),
    path('api/producto/destroy/<pk>/', views.ProductDestroyView.as_view(), name='delete_product'),
    path('api/producto/update/<pk>/', views.ProductUpdateView.as_view(), name =''),
]