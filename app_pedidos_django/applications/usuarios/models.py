from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from simple_history.models import HistoricalRecords


from .managers import UserManager




# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField('Nombre de usuario', unique = True, max_length=50)
    name = models.CharField('Nombre', max_length=50, blank=True,null=True)
    last_name = models.CharField('Apellidos', max_length=50, blank=True)
    email = models.EmailField('Correo electrónico',blank=False, unique=True)
    phone = models.CharField('Telefono', max_length=15)
    is_staff = models.BooleanField('Personal de la empresa',default=False)
    is_active = models.BooleanField('Estado de usuario',default=False)
    created_at = models.DateTimeField('Fecha creacion :',auto_now_add=True)
    updated_at = models.DateTimeField('Fecha actualizacion: ',auto_now=True)
    historical = HistoricalRecords()


    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email',]

    objects = UserManager()

    class Meta:
        """ Definición de la clase Meta para Usuario"""
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        ordering = ['username']
        db_table = 'User'
        unique_together = ['name','last_name','email']

    def get_short_name(self):
        return str(self.id)+' '+self.username
    
    def get_full_name(self):
        return str(self.id)+' '+self.name + ' ' + self.last_name

  
