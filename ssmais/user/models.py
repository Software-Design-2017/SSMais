# Django.
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from user import constants


class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(blank=False, max_length=constants.NAME_FIELD_LENGTH, default="")
    email = models.EmailField(unique=True)

    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_short_name(self):
        return self.name
