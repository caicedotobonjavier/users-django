from django.db import models
#
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
#
from .managers import UserManager
# Create your models here.

class User(AbstractBaseUser, PermissionsMixin):

    GENERO_CHOICES = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('O', 'Otros'),
    )
    
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField('Email')
    nombres = models.CharField('Nombres', max_length=30, blank=True, null=True)
    apellidos = models.CharField('Apellidos', max_length=30, blank=True, null=True)
    genero = models.CharField('Genero', max_length=1, choices=GENERO_CHOICES, blank=True, null=True)
    codigo = models.CharField('Codigo', max_length=6, default='000000')

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = UserManager()


    def get_fullname(self):
        return f'{self.nombres} {self.apellidos}'
    

    def get_shot_name(self):
        return self.username