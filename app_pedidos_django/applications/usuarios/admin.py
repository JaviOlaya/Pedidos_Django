from django.contrib import admin

# Register your models here.
from applications.usuarios.models import User

class UserAdmin(admin.ModelAdmin):

        list_display =(
            'username',
            'name',
            'last_name',
            'email',
            'phone', 
            'is_staff', 
            'is_active'
        )



admin.site.register(User, UserAdmin)