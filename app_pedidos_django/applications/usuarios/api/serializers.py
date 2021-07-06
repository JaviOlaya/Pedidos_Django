from rest_framework import serializers
from applications.usuarios.models import Usuario

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

