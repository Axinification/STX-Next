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


# class BookImportSerializer(serializers.Serializer):
#     external_id = serializers.CharField(max_length=30, null=True,
#                                         blank=True)
#     title = serializers.CharField()
#     authors = serializers.ListSerializer(
#         serializers.CharField(max_length=255, default=''), default=list)
#     published_year = serializers.CharField(max_length=4, default='')
#     acquired = serializers.BooleanField(default=False)
#     thumbnail = serializers.CharField(default='')

        # def validate(self, data):
        #     queryset = Book.objects.all()
        #     print(self.fields)
        #     external_id = self['external_id']
        #     if queryset.filter(external_id__exact=external_id).exists():
        #         raise ValidationErr()
            
        # validators = [
        #     UniqueTogetherValidator(
        #         queryset=Book.objects.all(),
        #         fields=['id', 'external_id']
        #     )
        # ]
        
        # def validate_external_id(self, value):
        #     # I assumed that you will that the string value, is a JSON object.
        #     external_id = json.loads(value).get('en', None)
        #     if (external_id and Book.objects.filter(external_id__exact=external_id).exists()):
        #         raise serializers.ValidationError("External Id already exists!")
        #     # You need to return the value in after validation.
        #     return value
        
    # validators = []


    # def create(self, validated_data):
    #     if id is not None:
    #         print(validated_data)
    #         validated_data.update({
    #             'id': validated_data.id
    #         })
    #     book = Book.objects.create(**validated_data)
    #     return book
