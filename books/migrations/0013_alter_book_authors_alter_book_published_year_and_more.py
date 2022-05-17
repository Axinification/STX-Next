# Generated by Django 4.0.4 on 2022-05-16 10:40

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0012_alter_book_published_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='authors',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=255, null=True), default=list, size=None),
        ),
        migrations.AlterField(
            model_name='book',
            name='published_year',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
