from django.db import models
#
from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager, models.Manager):
    
    def _create_user(self,username, email, password, is_staff, is_active, is_superuser, **extra_fields):
        user = self.model(
            username = username,
            email=email,
            is_staff=is_staff,
            is_active = is_active,
            is_superuser = is_superuser,
            **extra_fields
        )
        # Se encripta la contraseña
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user (self,username, email, password=None, **extra_fields):
        return self._create_user(username, email, password, False,True,False, **extra_fields)

    def create_superuser(self, username, email, password = None, **extrafields):
        return self._create_user(username, email, password,True,True, True, **extrafields)