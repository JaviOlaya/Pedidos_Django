from django.urls import path,include,re_path

from . import views 

app_name = 'usuarios_app'


urlpatterns = [
    path('logout/', views.Logout.as_view(), name = 'logout'),
    path('login/', views.Login.as_view(), name = 'Login'),
    path('api/usuario/list/', views.UserListAPIView.as_view()),
    path('api/usuario/create/', views.UserCreateView.as_view()),
    path('api/usuario/detail/<pk>/', views.UserRetrieveView.as_view()),
    path('api/usuario/destroy/<pk>/', views.UserDestroyView.as_view()),
    path('api/usuario/update/<pk>/', views.UserUpdateView.as_view()),
]