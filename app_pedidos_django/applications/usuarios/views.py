from django.shortcuts import render
from datetime import datetime

from django.views.generic import ListView, TemplateView

from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, DestroyAPIView, RetrieveUpdateAPIView

#Modelo de Usuario 
from .models import User

#serielizers
from .serializers import UserSerializer,UserLoginSerializer

from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken

from applications.usuarios.serializers import UserTokenSerializer


class Login(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        login_serializer = self.serializer_class(data = request.data, context = {'request':request})
        if login_serializer.is_valid():
            user=login_serializer.validated_data['user']
            if user.is_active:
                token,created = Token.objects.get_or_create(user = user)
                user_serializer = UserTokenSerializer(user)
                if created:
                    return Response({
                        'token': token.key,
                         'user': user_serializer.data,
                         'message':'Ha iniciado sesión correctamente.'
                        }, status  = status.HTTP_201_CREATED)
                
                else:
                    
                    # all_sessions=Session.objects,filter(expire_date__gte = datetime.now())
                    # if all_sessions.exists():
                    #     for session in all_sessions:
                    #         session_data = session.get_decoded()
                    #         if user.id == int(session_data.get('_auth_user_id')):
                    #             session.delete()
                    # token.delete()
                    # token= Token.objects.create(user = user)
                    # return Response({
                    #     'token': token.key,
                    #      'user': user_serializer.data,
                    #      'message':'Ha iniciado sesión correctamente.'
                    #     }, status  = status.HTTP_201_CREATED)

                    return Response({'error': 'Ya se ha iniciado sesion con este usuario'}, 
                        status = status.HTTP_409_CONFLICT)
            else:
                return Response({'error': 'Este no puede iniicar sesión'},
                        status = status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({'error': 'Nombre de usuario o contraseña incorrectos.'},
                        status = status.HTTP_400_BAD_REQUEST)    
        return Response({'mensaje':'Hola desde response'}, status = status.HTTP_200_OK)



class Logout(APIView):

    def get(self, request, *args, **kwargs):
        try:
            token = request.GET.get('token')
            token = Token.objects.filter(key = token).first()

            if token:
                user = token.user

                all_sessions=Session.objects,filter(expire_date__gte = datetime.now())
                if all_sessions.exists():
                    for session in all_sessions:
                        session_data = session.get_decoded()
                        if user.id == int(session_data.get('_auth_user_id')):
                            session.delete()

                token.delete()
                session_message = 'Sesiones de usuario eliminadas.'
                token_message = 'Token eliminado.'
                return Response({'token_message': token_message, 'session_message':session_message},
                                    status = status.HTTP_200_OK)

            return Response({'error':'No se ha encontrado un usuario con estas credenciales.'},
                            status = status.HTTP_400_BAD_REQUEST)
        except:
            return Response({'error':'No se ha encontrado token en la petición.'},
                                status = status.HTTP_409_CONFLICT)
       
        



class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    


class UserListAPIView(ListAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
      
        return User.objects.all()

class UserCreateView(CreateAPIView):
    serializer_class = UserSerializer

    def post(self, request):
        serializer = self.serializer_class(data)

class UserRetrieveView(RetrieveAPIView):
    
    serializer_class = UserSerializer
    queryset = User.objects.all()

class UserDestroyView(DestroyAPIView):
 
    serializer_class = UserSerializer
    queryset = User.objects.all()

class UserUpdateView(RetrieveUpdateAPIView):
    
    serializer_class = UserSerializer
    queryset = User.objects.all()