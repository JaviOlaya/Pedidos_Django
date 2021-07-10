from rest_framework.routers import DefaultRouter
from . import views
router = DefaultRouter()

router.register(r'productos/',views.ProductViewSet,basename ="products")

app_name = 'productos_app'

urlpatterns = router.urls
