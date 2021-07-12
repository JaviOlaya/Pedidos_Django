from rest_framework.routers import DefaultRouter
from . import views
router = DefaultRouter()

router.register(r'pedidos',views.OrderViewSet,basename ="pedidos")

app_name = 'pedidos_app'

urlpatterns = router.urls