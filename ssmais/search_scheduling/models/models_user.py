# Django.
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, password, name, **kwargs):
        if not email:
            raise ValueError('The given email must be set')

        user = self.model(email=self.normalize_email(email),
                          name=name,
                          is_active=False,
                          **kwargs)
        user.set_password(password)
        user.save(using=self.db)

        return user

    def create_superuser(self, email, password, name, **kwargs):
        user = self.model(email=self.normalize_email(email),
                          name=name,
                          is_staff=True,
                          is_active=True,
                          is_superuser=True,
                          **kwargs)

        user.set_password(password)
        user.save(using=self.db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(blank=False, max_length=80, default="")
    email = models.EmailField(unique=True)

    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    objects = UserManager()

    def get_short_name(self):
        return self.name
