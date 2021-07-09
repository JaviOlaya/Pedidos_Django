from rest_framework.routers DefaultRouter
from applications.productos.views import ProductViewSet

router = DefaultRouter()

router.register(r'producto/',ProductViewSet)

urlpatterns = router.urls
