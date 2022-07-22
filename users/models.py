from email.policy import default
from django.contrib.auth.models import AbstractUser
from django.db import models
from users.managers import CustomUserManager
from django.utils import timezone


class TypeUser(models.Model):

    name = models.CharField(max_length=255)


    def __str__(self) -> str:
        return f"{self.id}: {self.name}"





class Profile(AbstractUser):

    USER_STATUS_CHOICES = (
        ('registered','registered'),
        ('requested_to_driver','requested_to_driver'),
        ('allowed_drive','allowed_drive'),
        ('disallowed_drive','disallowed_drive')
    )

    
    phone = models.CharField('Phone',unique=True,max_length=255)
    type_user = models.ForeignKey(TypeUser,on_delete=models.CASCADE,null=True,blank=True)
    is_driver = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    status = models.CharField('Status',max_length=255,null=True,blank=True,choices=USER_STATUS_CHOICES,default='registered')
    driver_can_view_order_date = models.DateField(null=True,blank=True)
    username = None
    last_name = None
    first_name = None
    groups = None
    email = None
    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.phone



class ProfileInfo(models.Model):
    avatar = models.ImageField(upload_to='avatars/',null=True,blank=True)
    email = models.EmailField('email address', unique=True,null=True,blank=True)
    city = models.ForeignKey('regions.City',on_delete=models.CASCADE,related_name='users',null=True,blank=True)
    birthday = models.DateTimeField(null=True,blank=True)
    last_name = models.CharField('Last name',max_length=255,null=True,blank=True)
    first_name = models.CharField('First name',max_length=255,null=True,blank=True)
    user = models.OneToOneField(Profile,on_delete=models.CASCADE,related_name='profile_info')

class UserDocuments(models.Model):

    passport_photo_front = models.FileField(upload_to='user-pasports/')
    passport_photo_back = models.FileField(upload_to='user-passports/')
    car_passport = models.FileField(upload_to='car-passport/')
    user = models.OneToOneField(Profile,on_delete=models.CASCADE,related_name='user_document')


class ProfileLoginOTP(models.Model):

    profile = models.ForeignKey(Profile,on_delete=models.CASCADE)
    otp = models.IntegerField()
    created_at = models.DateTimeField(default=timezone.now)