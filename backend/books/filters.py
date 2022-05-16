from django_filters import rest_framework as filters
from .models import Book


class CharInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class BookFilter(filters.FilterSet):
    author = CharInFilter(field_name='authors', lookup_expr='icontains')
    title = filters.CharFilter(field_name='title', lookup_expr='icontains')

    class Meta:
        model = Book
        fields = ['title', 'author', 'acquired']
