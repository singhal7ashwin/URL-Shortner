from django.db import models

# Create your models here.
class Url(models.Model):
    original_url = models.CharField(max_length=10000)
    shortened_url = models.CharField(max_length=10)
