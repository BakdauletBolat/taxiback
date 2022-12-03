from rest_framework import serializers

from apps.message.models import Message, MessageType


class MessageTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MessageType
        fields = ('name', 'id')


class MessageSerializer(serializers.ModelSerializer):
    type = MessageTypeSerializer()

    class Meta:
        model = Message
        fields = ('title', 'text', 'created_at', 'is_read', 'type')
