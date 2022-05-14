from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.


class Book(models.Model):
    external_id = models.CharField(max_length=30, null=True, blank=True)
    title = models.CharField(max_length=120)
    authors = ArrayField(models.CharField(max_length=50), default=list)
    published_year = models.CharField(max_length=4)
    acquired = models.BooleanField(default=False)
    thumbnail = models.URLField(null=True, blank=True)
