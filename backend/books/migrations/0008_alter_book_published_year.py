# Generated by Django 4.0.4 on 2022-05-14 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0007_alter_book_published_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='published_year',
            field=models.CharField(max_length=4),
        ),
    ]
