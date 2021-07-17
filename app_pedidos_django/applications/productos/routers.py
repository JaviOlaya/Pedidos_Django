from rest_framework.routers import DefaultRouter
from . import views
router = DefaultRouter()

router.register(r'productos', views.ListProductViewSet, basename ="productos"),
router.register(r'productos/usuario', views.ListProductUserViewSet, basename ="productos"),
#router.register(r'productos/stock', views.ListProductStock, basename ="productos_stock"),

app_name = 'productos_app'

urlpatterns = router.urls
