# Generated by Django 4.0.4 on 2022-05-16 07:22

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0010_alter_book_external_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='authors',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=255), default=list, size=None),
        ),
        migrations.AlterField(
            model_name='book',
            name='external_id',
            field=models.CharField(blank=True, max_length=50, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=255),
        ),
    ]
