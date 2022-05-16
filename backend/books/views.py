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
    books = Book.objects
    # queryset.bulk_update(Book.objects.select_related('published_year'))
    filter_backends = [BooksSearchFilter]
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return BookDetailsSerializer
        return BookSimpleSerializer


class ImportAPIView(generics.CreateAPIView, generics.UpdateAPIView):
    def post(self, request):
        author = request.data['author']
        self.books_count = 0
        self.start_index = 0
        self.max_results = 40  # max 40
        books_url = f"""https://www.googleapis.com/books/v1/volumes?q={author}+inauthor&printType=books&startIndex={self.start_index}&maxResults={self.max_results}"""
        response = requests.get(books_url).json()
        self.total_items = response['totalItems']
        items = response['items']

        while self.total_items > 0:
            for item in items:
                info = item['volumeInfo']
                try:
                    book_data = {
                        'external_id': item['id'],
                        'title': info['title'],
                        'authors': info['authors'],
                        'published_year': info['publishedDate'][:4],
                        'thumbnail': info['imageLinks']['thumbnail'],
                    }
                    serializer = BookDetailsSerializer(data=book_data)
                    if serializer.is_valid(raise_exception=True):
                        serializer.save()
                        self.books_count += 1
                        # print(self.books_count)
                except Exception:
                    continue
            self.start_index += self.max_results
            if self.total_items >= self.max_results:
                self.total_items -= self.max_results
            else:
                self.total_items -= self.total_items
                print(self.total_items)
            books_url = f"""https://www.googleapis.com/books/v1/volumes?q={author}+inauthor&printType=books&startIndex={self.start_index}&maxResults={self.max_results}"""
            try:
                response = requests.get(books_url).json()
                items = response['items']
            except Exception as e:
                if e == 'items':
                    print(e)
                break
        return JsonResponse({'imported': self.books_count})
