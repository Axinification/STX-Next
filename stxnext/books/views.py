from django.http import JsonResponse
import requests
from .models import Book
from .serializers import BookDetailsSerializer, BookSimpleSerializer
from rest_framework import generics
from .filters import BooksSearchFilter


class BookRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView,
                                       generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookDetailsSerializer
    lookup_field = 'pk'


class BookListCreateAPIView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    filter_backends = [BooksSearchFilter]

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return BookDetailsSerializer
        return BookSimpleSerializer


class ImportAPIView(generics.CreateAPIView):
    def post(self, request):
        author = request.data['author']
        book_count = 0
        url = "https://www.googleapis.com/books/v1/volumes"
        query = f"?q={author}+inauthor"
        response = requests.get(url+query).json()
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
                published_year = int(info['publishedDate'][:4])
            except KeyError:
                published_year = 0

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
                print(e['external_id'])
                continue
        return JsonResponse({'imported': book_count})
