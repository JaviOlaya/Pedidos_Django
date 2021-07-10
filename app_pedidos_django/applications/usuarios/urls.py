from django.urls import path,include,re_path

from rest_framework.routers import DefaultRouter

from . import views 

app_name = 'usuarios_app'

router = DefaultRouter()


router.register(r'usuarios', views.USerViewSet, basename='usuarios' )

urlpatterns = [
    path('', include(router.urls)),
    path('api/usuario/list/', views.UserListAPIView.as_view()),
    path('api/usuario/create/', views.UserCreateView.as_view()),
    path('api/usuario/detail/<pk>/', views.UserRetrieveView.as_view()),
    path('api/usuario/destroy/<pk>/', views.UserDestroyView.as_view()),
    path('api/usuario/update/<pk>/', views.UserUpdateView.as_view()),
]