from django.core.exceptions import ValidationError
from rest_framework import serializers
from .models import Book


class BookSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = [
            'id',
            'title',
            'authors',
            'published_year',
            'acquired',
        ]


class BookImportSerializer(serializers.ModelSerializer):
    def validate_external_id(self, value):
        external_ids = list(Book.objects.all().values_list('external_id',
                                                           flat=True))
        if value in external_ids:
            raise ValidationError(
                {'external_id': "external_id has to be unique"})
        return value

    class Meta:
        model = Book
        fields = [
            'id',
            'external_id',
            'title',
            'authors',
            'published_year',
            'acquired',
            'thumbnail'
        ]


class BookDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = [
            'id',
            'external_id',
            'title',
            'authors',
            'published_year',
            'acquired',
            'thumbnail'
        ]
