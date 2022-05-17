from rest_framework import filters
from .serializers import BookFilterSerializer
from django.db.models.lookups import GreaterThanOrEqual, LessThanOrEqual
from django.db.models import F
from .models import Book
# from django_bulk_update.helper import bulk_update


class BooksSearchFilter(filters.BaseFilterBackend):
    serializer_class = BookFilterSerializer

    def filter_queryset(self, request, queryset):
        from_year = request.GET.get('from', None)
        to_year = request.GET.get('to', None)
        author = request.GET.get('author', None)
        title = request.GET.get('title', None)
        books = Book.objects.all()
        if author is not None:
            queryset = books.filter(authors__icontains=author)
        if from_year is not None:
            queryset = books.filter(GreaterThanOrEqual(
                                       int(F('published_year')), from_year))
        if to_year is not None:
            queryset = books.filter(LessThanOrEqual(
                                       int(F('published_year')), to_year))
        if title is not None:
            queryset = books.filter(title__icontains=title)
        return queryset()
