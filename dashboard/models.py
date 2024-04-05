from django.db import models


class Broker(models.Model):
    name = models.CharField(max_length=50)
    url = models.CharField(max_length=255)
    description = models.TextField( blank=True, null=True)
    # message = models.TextField()
    date = models.DateField()
    image_url = models.CharField(max_length=2083, blank=True, null=True)

