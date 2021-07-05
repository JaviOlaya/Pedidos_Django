from django.urls import path

from rest_framework.routers import DefaultRouter

from . import views

app_name = 'usuarios_app'

router = DefaultRouter()

router.register(r'usuarios', user_views.USerViewSet, basename='usuarios' )

urlpatterns = [
    path('', include(router.urls)),
    path('api/usuario/list/', views.UsuarioListAPIView.as_view()),
    path('api/usuario/create/', views.UsuarioCreateView.as_view()),
    path('api/usuario/detail/<pk>/', views.UsuarioRetrieveView.as_view()),
    path('api/usuario/destroy/<pk>/', views.UsuarioDestroyView.as_view()),
    path('api/usuario/update/<pk>/', views.UsuarioUpdateView.as_view()),
]