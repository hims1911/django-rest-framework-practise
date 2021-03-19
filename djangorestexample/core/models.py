from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import PermissionsMixin
from django.core.validators import MaxLengthValidator, MinLengthValidator,RegexValidator
from .managers import CustomUserManager

# Create your models here.
class User(AbstractUser):
    email = models.EmailField(
        unique=True,
        max_length=254,
    )
    username = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    name = models.CharField(max_length=30, unique=True)
    mobile = models.CharField(unique=True, max_length=10)
    pincode = models.CharField(max_length=6,validators=[RegexValidator('^\d+$', message="Password should be a combination of Alphabets and Numbers"), MinLengthValidator(6, message="minimum length should be 6 and max too")])
    city = models.CharField(max_length=200, null=True)

    objects = CustomUserManager()

    def __str__(self):
        return self.email



