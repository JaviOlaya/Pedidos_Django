from django.contrib import admin

# Register your models here.
from applications.usuarios.models import User


admin.site.register(User)