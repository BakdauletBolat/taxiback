from django.db import models


class Car(models.Model):
    name = models.CharField('Имя', unique=True, max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Машина'
        verbose_name_plural = 'Машины'


class CarModel(models.Model):
    name = models.CharField('Имя', unique=True, max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Модель'
        verbose_name_plural = 'Модели'


class CarInfo(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    model = models.ForeignKey(CarModel, on_delete=models.CASCADE)
    year = models.CharField(max_length=255, null=True, blank=True)
    number = models.CharField(max_length=255)
    color = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"{self.car.name}: {self.model.name} - {self.number}"

    class Meta:
        verbose_name = 'Инфо о машине'
        verbose_name_plural = 'Инфо о машине'
