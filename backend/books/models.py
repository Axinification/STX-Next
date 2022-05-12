from django.db import models

# Create your models here.


class Book(models.Model):
    id = models.AutoField(primary_key=True)
    external_id = models.CharField(max_length=30)
    title = models.CharField(max_length=120)
    authors = models.CharField(max_length=120)
    published_year = models.CharField(max_length=4)
    acquired = models.BooleanField(default=False)
    thumbnail = models.URLField(null=True, blank=True)
