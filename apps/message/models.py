from django.db import models

from apps.users.models import User


class Message(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    is_read = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Сообщение'
