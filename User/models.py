from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from .managers import CustomUserManager


class PetCareUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    contactNo = models.IntegerField(blank=True, null=True)
    petName = models.CharField(max_length=50, blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
