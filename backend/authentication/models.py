from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class UserManager(BaseUserManager):
    def _create_user(self, email, password=None, user_type=None, **extra_fields):
        if not email:
            raise ValueError("Email field must be set.")
        email = self.normalize_email(email)
        user = self.model(email=email, user_type=user_type, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, user_type=None, **extra_fields):
        return self._create_user(email, password, user_type, **extra_fields)

    def create_superuser(self, email, password=None, user_type=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        return self._create_user(email, password, user_type, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):


    email = models.EmailField(max_length=250, unique=True)
    user_type = models.CharField(max_length=20)  
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'user_type']

    objects = UserManager()
