from django.db import models


# Create your models here.

class FeedBack(models.Model):
    image = models.ImageField(upload_to='form-images/')
    email = models.EmailField()
    text = models.TextField(null=True, blank=True)

    def __str__(self):
        message = f'Отзыв от: {self.email}'
        return message
