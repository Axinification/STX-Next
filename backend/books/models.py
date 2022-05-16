from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.


class Book(models.Model):
    external_id = models.CharField(max_length=50, null=True,
                                   blank=True, unique=True)
    title = models.CharField(max_length=255, null=True, blank=True)
    authors = ArrayField(models.CharField(max_length=255, null=True,
                                          blank=True, default=None
                                          ), default=list)
    published_year = models.CharField(max_length=4, null=True,
                                      blank=True, default=None)
    acquired = models.BooleanField(default=False)
    thumbnail = models.TextField(null=True, blank=True)

    # def year_to_int(self):
    #     return int(self.published_year)
