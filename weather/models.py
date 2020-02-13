from django.db import models


class Weather(models.Model):
    city_name = models.CharField(max_length=250)
    summary = models.CharField(max_length=100)
    temperature = models.FloatField(default=0.0)

    def __str__(self):
        return self.city_name
