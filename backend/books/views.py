from django.http import JsonResponse
import requests
from .models import Book
from .serializers import BookDetailsSerializer, BookSimpleSerializer
from rest_framework import generics


class BookRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView,
                                       generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookDetailsSerializer
    lookup_field = 'pk'


class BookListCreateAPIView(generics.ListCreateAPIView):

    def get_queryset(self):
        queryset = Book.objects.all()
        return queryset

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return BookDetailsSerializer
        return BookSimpleSerializer


class ImportAPIView(generics.CreateAPIView):
    def post(self, request):
        author = request.data['author']
        a = f"https://www.googleapis.com/books/v1/volumes?q={author}+inauthor"
        response = requests.get(a).json()
        items = response['items']
        for item in items:
            info = item['volumeInfo']
            try:
                thumbnail = info['imageLinks']['thumbnail']
            except KeyError:
                thumbnail = "None provided"
            try:
                title = f"{info['title']} {info['subtitle']}"
            except KeyError:
                title = info['title']
            finally:
                book_data = {
                    'external_id': item['id'],
                    'title': title,
                    'authors': info['authors'],
                    'published_year': int(info['publishedDate'][:4]),
                    'thumbnail': thumbnail,
                }
                serializer = BookDetailsSerializer(data=book_data)
                if serializer.is_valid(raise_exception=True):
                    serializer.save()
        return JsonResponse({'imported': len(items)})
