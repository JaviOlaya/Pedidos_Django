from .models import User
from django.contrib.auth import password_validation, authenticate
from django.core.validators import RegexValidator


# Django REST Framework
from rest_framework import serializers, pagination
from rest_framework.authtoken.models import Token
from rest_framework.validators import UniqueValidator


class UserTokenSerializer(serializers.ModelSerializer):
      class Meta:
            model = User
            fields = ('username','email','name','last_name')
class UserSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = User
        fields =(
          '__all__'
        )
    
    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
    
    def update(self, instance, validated_data):
          updated_user = super().update(instance, validated_data)
          updated_user.set_password(validated_data['password'])
          updated_user.save()
          return updated_user

class UserListSerializer(serializers.ModelSerializer):
      class Meta:
          model = User
      
      def to_representation(self, instance):
            return{
              'id': instance['id'],
              'username': instance['username'],
              'email': instance['email'],
              'password': instance['password']
            }

class USerSignUpSerializer(serializers.Serializer):
      
      email = serializers.EmailField(
        validators = [UniqueValidator(queryset=User.objects.all())]
      )

      username = serializers.CharField(
        min_length = 4,
        max_length = 20,
        validators =[UniqueValidator(queryset = User.objects.all())]
      )

class UserLoginSerializer(serializers.Serializer):

  #Vamos a requerir 
  email =  serializers.EmailField()
  password = serializers.CharField(min_length=6, max_length=64)


#Validación de datos
  def validate(self, data):
  
    user = authenticate(username=data['email'], password = data['password'])

    if not user:
      raise serializers.ValidationError('Los datos del usuario no son correctos')

#Guardamos el usuario
    self.context['user'] = user 
    return data

  def create(self,data):
    """Generar o recuperar token """
    token, created = Token.objects.get_or_create(user=self.context['user'])
    return self.context['user'], token.key



class PaginationSerializer(pagination.PageNumberPagination):

    page_size = 5
    max_page_size = 10
