from django.db import models
from django.contrib.postgres.fields import ArrayField


class Book(models.Model):
    external_id = models.CharField(max_length=30, null=True, blank=True)
    title = models.TextField(null=False)
    authors = ArrayField(models.TextField(), default=list)
    published_year = models.CharField(max_length=4, default='')
    acquired = models.BooleanField(default=False)
    thumbnail = models.TextField(default='')
