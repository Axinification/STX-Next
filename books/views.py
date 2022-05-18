from django.http import JsonResponse
import requests
from .models import Book
from .serializers import BookDetailsSerializer, BookSimpleSerializer
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
            'pubished_date': int(self.get_author()),
        }

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return BookDetailsSerializer
        return BookSimpleSerializer


class ImportAPIView(generics.CreateAPIView):
    def post(self, request):
        author = request.data['author']
        book_count = 0
        start_index = 0
        max_results = 40
        page = get_url_string(author, start_index, max_results)
        response = requests.get(page).json()
        total_items = response['totalItems']
        while total_items > 0:
            items = response['items']
            for item in items:
                info = item['volumeInfo']

                try:
                    title = f"{info['title']} {info['subtitle']}"
                except KeyError:
                    title = info['title']

                try:
                    thumbnail = info['imageLinks']['thumbnail']
                except KeyError:
                    thumbnail = "None provided"

                try:
                    authors = info['authors']
                except KeyError:
                    authors = ['']

                try:
                    published_year = info['publishedDate'][:4]
                except KeyError:
                    published_year = ""

                try:
                    book_data = {
                        'external_id': item['id'],
                        'title': title,
                        'authors': authors,
                        'published_year': published_year,
                        'thumbnail': thumbnail,
                    }
                    serializer = BookDetailsSerializer(data=book_data)
                    if serializer.is_valid():
                        serializer.save()
                        book_count += 1
                    else:
                        continue
                except KeyError as e:
                    print(e)
                    continue
            total_items -= max_results
            start_index += max_results
            get_url_string(author, start_index, max_results)
            response = requests.get(page).json()
        return JsonResponse({'imported': book_count})
