from model_utils.models import TimeStampedModel
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin


from simple_history.models import HistoricalRecords

# Create your models here.


class UserManager(BaseUserManager):
    def_create_user(self, username, name, last_name, email, password, is_staff, is_superuser,**extra_fields):
        user = self.model(
            username = username,
            name = name,
            last_name = last_name,

        )

class User(TimeStampedModel, AbstractBaseUser, PermissionsMixin):
    username = models.CharField('Nombre de usuario', unique = True, max_length=100,required=True)
    name = models.CharField('Nombre', max_length=50, blank=True)
    last_name = models.CharField('Apellidos', max_length=50, blank=True)
    email = models.EmailField('Correo electrónico',blank=False, unique=True, required=True)
    phone = models.CharField('Telefono', max_length=15)
    password = models.CharField('Contraseña', max_length=64,null=True, blank=True, required=True)
    is_superuser = models.BooleanField('Usuario administrador', default=False)
    is_active = models.BooleanField('Usuario activo',default = True)


    class Meta:

        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'


    USERNAME_FIELD = 'username'


    def natural_key(self):
        return(self.username)

    def __str__(self):
        return "Usuario {0}, nombre completo: {1} {2}".format(self.username, self.name, self.last_name)

  
