from django.contrib import admin

from users.models import Profile, ProfileInfo, ProfileLoginOTP, UserDocuments



admin.site.register(ProfileLoginOTP)



class ProfileInfoTabularInline(admin.StackedInline):
    model = ProfileInfo

class UserDocumentsTabularInline(admin.StackedInline):   
    model = UserDocuments

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('phone','status','is_driver','type_user')
    list_editable = ('status',)
    fields = ('phone','status','is_driver','type_user')
    inlines = (ProfileInfoTabularInline,UserDocumentsTabularInline)

admin.site.register(Profile,ProfileAdmin)
admin.site.register(ProfileInfo)
admin.site.register(UserDocuments)