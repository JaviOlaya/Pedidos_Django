from django.urls import path,include,re_path

from . import views 

app_name = 'usuarios_app'


urlpatterns = [
    path('logout/', views.Logout.as_view(), name = 'logout'),
    path('login/', views.Login.as_view(), name = 'Login'),
  
]