from rest_framework import filters


class BooksSearchFilter(filters.BaseFilterBackend):
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
