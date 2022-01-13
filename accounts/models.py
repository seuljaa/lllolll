from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

class UserManager(BaseUserManager):
    def create_user(self, username, email=None, password=None, **extra_fields):
        user = self.model(
        username=username,
        email=email,
        )
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        user.set_password(password)
        user.is_active = False
        user.save()
        return user

    def create_superuser(self, username, email=None, password=None, **extra_fields):
        superuser = self.create_user(
        username=username,
        password=password,
        email=email,
        )
        superuser.is_admin = True
        superuser.is_superuser = True
        superuser.is_active = True
        superuser.is_staff = True
        superuser.save()
        return superuser

class User(AbstractBaseUser):
# Default : id / password / last_login
    SERVER_CHOICES = (
        ('scania', '스카니아'),
        ('bera', '베라'),
        ('luna', '루나'),
        ('zenith', '제니스'),
        ('croa', '크로아'),
        ('union', '유니온'),
        ('elysium', '엘리시움'),
        ('enosis', '이노시스'),
        ('red', '레드'),
        ('aurora', '오로라'),
        ('arcane', '아케인'),
        ('nova', '노바'),
    )

    email = models.EmailField(max_length=100, null=False)
    username = models.CharField(max_length=20, unique=True)
    server = models.CharField(max_length=9, choices=SERVER_CHOICES)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
    objects = UserManager()

    def has_module_perms(self, app_label):
        return True


    def has_perm(self, perm, obj=None):
        return True


