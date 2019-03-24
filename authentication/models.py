from uuid import uuid4
from django.db import models, transaction
from django.utils import timezone
from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin, BaseUserManager
)


class UserManager(BaseUserManager):

    def _create_user(self, name, **extra_fields):
        """
        Creates and saves a User with the given email,and password.
        """
        if not name:
            raise ValueError('The given username must be set')
        try:
            with transaction.atomic():
                user = self.model(name=name, **extra_fields)
                user.save(using=self._db)
                return user
        except:
            raise


class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, unique=True, null=False, default=uuid4)
    name = models.CharField(max_length=120, unique=True, null=False)
    role = models.CharField(max_length=20, null=True)
    date_joined = models.DateTimeField(default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = 'name'

    def save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)
        return self
