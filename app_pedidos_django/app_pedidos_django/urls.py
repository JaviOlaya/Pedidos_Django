"""app_pedidos_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from django.conf.urls.static import static
from  applications.usuarios.views import Login, Logout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('logout/', Logout.as_view(), name = 'logout'),
    path('login/', Login.as_view(), name = 'Login'),
    re_path('', include(('applications.usuarios.urls'),namespace = 'users')),
    re_path('', include(('applications.productos.routers'), namespace='products')),
    re_path('', include(('applications.pedidos.urls'), namespace='orders')),
]
