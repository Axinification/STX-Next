from django_filters import rest_framework as filters
from rest_framework import filters as rest_filters


class BookFilterBackend(filters.DjangoFilterBackend):
    def get_filterset_kwargs(self, request, queryset, view):
        kwargs = super().get_filterset_kwargs(request, queryset, view)
        # merge filterset kwargs provided by view class
        if hasattr(view, 'get_filterset_kwargs'):
            kwargs.update(view.get_filterset_kwargs())
        return kwargs


class BooksSearchFilter(rest_filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        from_year = request.GET.get('from', None)
        to_year = request.GET.get('to', None)
        author = request.GET.get('author', None)
        title = request.GET.get('title', None)
        print(from_year, to_year)
        if author is not None:
            queryset = queryset.filter(authors__icontains=author)
        if from_year is not None:
            queryset = queryset.filter(published_year__gte=from_year)
        if to_year is not None:
            queryset = queryset.filter(published_year__lte=to_year)
        if title is not None:
            queryset = queryset.filter(title__icontains=title)
        return queryset
