from django.db import models

class Region(models.Model):

    name = models.CharField(max_length=255)


class City(models.Model):

    name = models.CharField(max_length=255)
    region = models.ForeignKey(Region,on_delete=models.CASCADE)