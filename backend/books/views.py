import requests
from rest_framework import generics
# from rest_framework.decorators import api_view
from rest_framework.response import Response
# from django.shortcuts import get_object_or_404
from .models import Book
from .serializers import BookDetailsSerializer, BookSimpleSerializer
from rest_framework import filters
from .filters import BookFilter


class BookRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView,
                                       generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookDetailsSerializer
    lookup_field = 'pk'


class BookListCreateAPIView(generics.ListCreateAPIView):
    filterset_class = BookFilter
    queryset = Book.objects.all()
    filter_backends = [filters.SearchFilter]

    def get_queryset(self):
        queryset = Book.objects.all()
        titles = queryset.only('title')
        authors = queryset.only('authors')
        years = queryset.only('published_year')
        from_year = self.request.GET.get('from')
        to_year = self.request.GET.get('to')
        author = self.request.GET.get('author')
        title = self.request.GET.get('title')

        if author is not None:
            queryset = queryset.filter(author__in=authors)
        if from_year is not None:
            queryset = queryset.filter(from_year__gt=years)
        if to_year is not None:
            queryset = queryset.filter(from_year__lt=years)
        if title is not None:
            queryset = queryset.filter(title__in=titles)

    #     return queryset

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return BookDetailsSerializer
        return BookSimpleSerializer


class ImportAPIView(generics.CreateAPIView):
    def post(self, request):
        author = request.data['author']
        a = f"https://www.googleapis.com/books/v1/volumes?q={author}+inauthor"
        response = requests.get(a).json()
        totalItems = response['totalItems']
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
                    return Response(totalItems)
                return Response(serializer.errors)
            # except KeyError:
            #     print("Failed to get data")
            #     pass
            # else:
            #     book_data.save()

        # serializer = self.get_serializer(data=item)
        #     if serializer.is_valid(raise_exception=True):
        #         serializer.save(
        #             external_id=item["id"],
        #             title=info["title"]+info["subtitle"],
        #             authors=info["authors"],
        #             published_year=int(info["publishedDate"][:4]),
        #             thumbnail=info["imageLinks"]["thumbnail"],
        #         )


# book_list_create_view = BookListCreateAPIView.as_view()

# class BookDetailAPIView(generics.RetrieveAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer


# book_detail_view = BookDetailAPIView.as_view()


# class BookUpdateAPIView(generics.UpdateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#     lookup_field = 'pk'


# book_update_view = BookUpdateAPIView.as_view()


# class BookDestroyAPIView(generics.DestroyAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#     lookup_field = 'pk'

#     def perform_destroy(self, instance):
#         # instance = serializer.save()
#         return super().perform_destroy(instance)


# book_destroy_view = BookDestroyAPIView.as_view()


# class BookMixinView(
#     mixins.RetrieveUpdate
#     generics.GenericAPIView
# ):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#     lookup_field = 'pk'

#     def get(self, request, *args, **kwargs):
#         pk = kwargs.get('pk')
#         if pk is not None:
#             return self.retrieve(request, *args, **kwargs)
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.post(request, *args, **kwargs)

#     def patch(self, request, *args, **kwargs):
#         return self.patch(request, *args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#         return self.delete(request, *args, **kwargs)


# book_mixin_view = BookMixinView.as_view()

# @api_view(['GET', 'POST', 'PATCH', 'DELETE'])
# def book_composite_view(request, pk=None, *args, **kwargs):
#     """
#         Used for CRUD method selection
#     """
#     method = request.method
    

#     if method == 'GET':
#         if pk is not None:
#             # item detail view
#             return book_detail_view
#         # items list view
#         return book_list_create_view
#     elif method == 'POST':
#         # create an item
#         return book_list_create_view
#     elif method == 'PATCH':
#         # update an item
#         return book_update_view
#     elif method == 'DELETE':
#         # delete an item
#         return book_destroy_view
