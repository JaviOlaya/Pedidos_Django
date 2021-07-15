from rest_framework.routers import DefaultRouter
from . import views
router = DefaultRouter()

router.register(r'usuarios', views.UserViewSet, basename ="usuarios")

app_name = 'usuarios_app'

urlpatterns = router.urls