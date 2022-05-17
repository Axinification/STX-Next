from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.core.validators import MaxValueValidator

# Create your models here.

# TODO left published year in Integer for deployment, will work on filtering with string next


class Book(models.Model):
    external_id = models.CharField(max_length=30, null=True,
                                   blank=True, unique=True)
    title = models.CharField(max_length=120)
    authors = ArrayField(models.CharField(max_length=50), default=list)
    published_year = models.IntegerField(validators=[MaxValueValidator(9999)])
    acquired = models.BooleanField(default=False)
    thumbnail = models.TextField(null=True, blank=True)
