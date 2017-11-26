import datetime

# Django.
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db.models import EmailField
from django.core import validators
from . import constants


class UserManager(BaseUserManager):
    def create_user(self, email, password, name, **kwargs):

        if not email:
            raise ValueError('The given email must be set')

        email = self.normalize_email(email)
        user = self.model(email=email,
                          name=name,
                          is_active=False,
                          **kwargs)
        user.set_password(password)
        user.save(using=self.db)

        return user

    def create_superuser(self, email, password, name, **kwargs):

        email = self.normalize_email(email)
        user = self.model(email=email,
                          name=name,
                          is_staff=True,
                          is_active=True,
                          is_superuser=True,
                          **kwargs)

        user.set_password(password)
        user.save(using=self.db)

        return user


class Email(EmailField):
    validator = validators.EmailValidator(message=constants.EMAIL_FORMAT)

    default_validators = [validator]

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = constants.EMAIL_FIELD_LENGTH
        kwargs['default'] = ''
        kwargs['unique'] = True
        super(EmailField, self).__init__(*args, **kwargs)


class Name(models.CharField):
    validator_max_length = validators.MaxLengthValidator(constants.NAME_FIELD_LENGTH,
                                                         message=constants.NAME_SIZE)
    validator_format = validators.RegexValidator(regex=r'^[a-zA-Zá-úÀ-Úã-õ-Ã-Õ ]+$',
                                                 message=constants.NAME_CHARACTERS)

    default_validators = [validator_max_length, validator_format]

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 60
        kwargs['default'] = ''
        super(models.CharField, self).__init__(*args, **kwargs)


class User(AbstractBaseUser, PermissionsMixin):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    email = Email()
    name = Name()
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    objects = UserManager()

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    activation_key = models.CharField(max_length=40, blank=True)
    key_expires = models.DateTimeField(default=datetime.date.today())

    def __str__(self):
        return self.user.email

    class Meta:
        verbose_name_plural = u'Perfil de Usuario'
