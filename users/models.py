from django.contrib.auth.models import AbstractUser
from django.db import models
from users.managers import CustomUserManager
from django.utils import timezone


class UserType(models.Model):

    name = models.CharField(max_length=255)


class Profile(AbstractUser):
    email = models.EmailField('email address', unique=True,null=True,blank=True)
    phone = models.CharField('Phone',unique=True,max_length=255)
    user_type = models.ForeignKey(UserType,on_delete=models.CASCADE,null=True,blank=True)
    date_joined = models.DateTimeField(default=timezone.now)
    city = models.ForeignKey('regions.City',on_delete=models.CASCADE,related_name='users',null=True,blank=True)
    birthday = models.DateTimeField(null=True,blank=True)
    last_name = models.CharField('Last name',max_length=255,null=True,blank=True)
    first_name = models.CharField('First name',max_length=255,null=True,blank=True)
    username = None
    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.phone


class ProfileLoginOTP(models.Model):

    profile = models.ForeignKey(Profile,on_delete=models.CASCADE)
    otp = models.IntegerField()
    created_at = models.DateTimeField(default=timezone.now)