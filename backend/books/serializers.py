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


class BookFilterSerializer(serializers.ModelSerializer):
    # to_int = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Book
        fields = [
            'id',
            'title',
            'authors',
            'published_year',
            'acquired',
            # 'to_int'
        ]

    # def get_to_int(self, obj):
    #     return obj.year_to_int()


class BookDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

        # def get_to_int(self, obj):
        #     return obj.year_to_int()
