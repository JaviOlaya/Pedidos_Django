from rest_framework.routers import DefaultRouter
from . import views
router = DefaultRouter()

router.register(r'usuarios', views.UserViewSet, basename ="usuarios")
#router.register(r'login', views.Login, basename ="login")

app_name = 'usuarios_app'

urlpatterns = router.urls