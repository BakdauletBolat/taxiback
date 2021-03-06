from django.db import models

class Region(models.Model):

    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self) -> str:
        return f"{self.id}: {self.name}"


class City(models.Model):

    name = models.CharField(max_length=255)
    status = models.IntegerField(null=True,blank=True)
    region = models.ForeignKey(Region,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self) -> str:
        return f"{self.id}: {self.name} - {self.region.name}"