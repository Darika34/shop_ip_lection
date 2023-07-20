import email

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth. base_user import BaseUserManager
# Create your models here.

class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **kwargs):
        if not email:
            return ValueError('email not found')
        email = self.normalize_email(email=email)
        user = self.model(email=email, **kwargs)
        user.create_activation_code()
        user.set_password(password)#heshiruet pass
        user.save()
        return user

    def create_user(self, email, password, **kwargs):
        kwargs.setdefault('is_staff',False)
        kwargs.setdefault('is_superuser', False)
        return self._create_user(email=email, password=password, **kwargs)

    def create_superuser(self,email, password, **kwargs):
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_superuser', True)
        kwargs.setdefault('is_active', True)
        if kwargs.get('is_staff') is not True:
            raise ValueError('superuser should have a is_staff = True')
        if kwargs.get('is_superuser') is not True:
            raise ValueError('superuser should have a is_superuser = True')
        return self._create_user(email=email, password=password, **kwargs)





#         abstractUser used for rewrite user
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=150)
    activation_code = models.CharField(max_length=250, blank=True)
    username = models.CharField(max_length=100, blank=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    avatar = models.ImageField(upload_to='avatars', blank=True)
    is_active = models.BooleanField(default=False, help_text="okokkokokolallalallal")
    # help_text - поле служить для дачи инструcty для этого поля
    objects = UserManager() #my perepisivaem objects
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [] #obyazatelnoe pole


    def __str__(self):
        return self.email

    def create_activation_code(self):
        import uuid
        code = str(uuid.uuid4())
        self.activation_code = code