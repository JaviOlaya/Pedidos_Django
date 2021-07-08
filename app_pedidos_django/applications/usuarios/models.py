from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

#from simple_history.models import HistoricalRecords


from .managers import UserManager


# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField('Nombre de usuario', unique = True, max_length=50)
    name = models.CharField('Nombre', max_length=50, blank=True,null=True)
    last_name = models.CharField('Apellidos', max_length=50, blank=True)
    email = models.EmailField('Correo electrónico',blank=False, unique=True)
    phone = models.CharField('Telefono', max_length=15)
    password = models.CharField('Contraseña', max_length=64)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField('Usuario activo',default = True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
#    historical = HistoricalRecords()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email',]

    objects = UserManager()

    class Meta:
    
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'


    def get_short_name(self):
        return self.username
    
    def get_full_name(self):
        return self.name + ' ' + self.last_name

  
