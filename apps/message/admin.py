from django.contrib import admin

from apps.message.models import Message, MessageType

# Register your models here.
admin.site.register(Message)
admin.site.register(MessageType)
