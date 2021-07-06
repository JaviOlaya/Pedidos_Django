from rest_framework.views import ListAPIView
from rest_framework.response import Response
from .serializers import UserSerializer
from applications.usuarios.models import Usuario


class UsersAPIView(APIView):

    def get(self, request):
        users = Usuario.objects.all()
        users_serializer = UserSerializer(users, many = True)
        return Response(users_serializer)