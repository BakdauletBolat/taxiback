from rest_framework import serializers

from apps.message.models import Message


class MessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields = ('title', 'text', 'created_at', 'is_read')
