from django.http import JsonResponse
import requests
from .models import Book
from .serializers import BookDetailsSerializer, BookImportSerializer, BookSimpleSerializer
from rest_framework import generics
from .filters import BookFilterBackend, BooksSearchFilter
from .utils import get_url_string


class BookRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView,
                                       generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookDetailsSerializer
    lookup_field = 'pk'


class BookListCreateAPIView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    filter_backends = [BooksSearchFilter, BookFilterBackend]

    def get_filterset_kwargs(self):
        return {
            'pubished_date': int(self.get_published_date()),
        }

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return BookDetailsSerializer
        return BookSimpleSerializer


class ImportAPIView(generics.CreateAPIView, generics.UpdateAPIView):
    def post(self, request):
        author = request.data['author']
        self.book_count = 0
        start_index = 0
        max_results = 40
        page = get_url_string(author, start_index, max_results)
        response = requests.get(page).json()
        total_items = response['totalItems']
        while total_items > 0:
            items = response['items']
            print(items)
            for item in items:
                external_id = item['id']
                info = item['volumeInfo']
                title = info['title']
                authors = ['']
                published_year = ''
                thumbnail = ''

                try:
                    title = f"{info['title']} {info['subtitle']}"
                except KeyError:
                    continue

                try:
                    thumbnail = info['imageLinks']['thumbnail']
                except KeyError:
                    continue

                try:
                    authors = info['authors']
                except KeyError:
                    continue

                try:
                    published_year = info['publishedDate'][:4]
                except KeyError:
                    continue

                book_data = {
                        'external_id': external_id,
                        'title': title,
                        'authors': authors,
                        'published_year': published_year,
                        'thumbnail': thumbnail,
                    }

                serializer = BookImportSerializer(data=book_data)
                if serializer.is_valid():
                    self.book_count = self.book_count + 1
                    print(self.book_count)
                    serializer.save()

            total_items -= max_results
            start_index += max_results
            page = get_url_string(author, start_index, max_results)
            response = requests.get(page).json()
        return JsonResponse({'imported': self.book_count})
