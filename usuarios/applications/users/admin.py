from django.contrib import admin
#
from .models import User
# Register your models here.


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'username',
        'email',
        'nombres',
        'apellidos',
        'genero',
        'is_superuser',
        'is_staff',
        'is_active',
    )
