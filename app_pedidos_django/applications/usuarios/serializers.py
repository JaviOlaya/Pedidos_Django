from .models import Usuario
from django.contrib.auth import password_validation, authenticate


# Django REST Framework
from rest_framework import serializers
from rest_framework.authtoken.models import Token


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields =(
          '__all__'
        )

class UsuarioLoginSerializer(serializers.Serializer):

  #Vamos a requerir 
  email =  serializers.EmailField()
  password = serializers.CharField(min_length = 6, max_length=64)


#Validación de datos
  def validate(sel, data):
  
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