from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.


class User(models.Model):
    email = models.EmailField(verbose_name='email', max_length=60, unique=True)
    password = models.CharField(max_length=60)
    name = models.CharField(max_length=60)
    username = models.CharField(max_length=30, unique=True)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', ]

    def __str__(self):
        return self.email


class Event(models.Model):
    name = models.CharField(max_length=60)
    description = models.CharField(max_length=140)
    venue = models.CharField(max_length=60)
    time = models.DateTimeField(verbose_name='time of event')

    def __str__(self):
        return self.name


# class AccountManager(BaseUserManager):
#     def create_user(self, email, username, password):
#         if not email:
#             raise ValueError("Users must have an email address")
#         if not username:
#             raise ValueError("Users must have a username")
#         if not password:
#             raise ValueError("Users must have a password")

#         user = self.model(
#                email=self.normalize_email(email),
#                username=username,
#             )

#         user.set_password(password)
#         user.save(using=self._db)

#         return user

#     def create_superuser(self, email, username, password):
#         user = self.create_user(
#                email=self.normalize_email(email),
#                username=username,
#                password=password
#             )

#         user.is_admin = True
#         user.is_staff = True
#         user.is_superuser = True
#         user.save(using=self._db)

#         return user


# class Account(AbstractBaseUser):
#     email = models.EmailField(verbose_name='email', max_length=60, unique=True)
#     username = models.CharField(max_length=30, unique=True)
#     date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
#     last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
#     is_admin = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)
#     is_superuser = models.BooleanField(default=False)

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['username', ]
    
#     objects = AccountManager()

#     def __str__(self):
#         return self.email

#     def has_perm(self, perm, obj=None):
#         return self.is_admin

#     def has_module_perms(self, app_label):
#         return True
