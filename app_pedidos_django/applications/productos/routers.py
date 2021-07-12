from rest_framework.routers import DefaultRouter
from . import views
router = DefaultRouter()

router.register(r'productos', views.ProductViewSet, basename ="productos")

app_name = 'productos_app'

urlpatterns = router.urls
