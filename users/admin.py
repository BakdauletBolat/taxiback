from django.contrib import admin

from users.models import Profile, ProfileLoginOTP

# Register your models here.

admin.site.register(ProfileLoginOTP)
admin.site.register(Profile)