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

class BookDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    # def create(self, validated_data):
    #     if id is not None:
    #         print(validated_data)
    #         validated_data.update({
    #             'id': validated_data.id
    #         })
    #     book = Book.objects.create(**validated_data)
    #     return book
