from rest_framework.routers import DefaultRouter
from .views import OrderViewSet
router = DefaultRouter()

router.register(r'pedidos',OrderViewSet,basename ="pedidos")

app_name = 'pedidos_app'

urlpatterns = router.urls