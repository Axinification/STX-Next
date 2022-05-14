from rest_framework import generics
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from django.shortcuts import get_object_or_404
from .models import Book
from .serializers import BookSerializer


class BookRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView,
                                       generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'pk'


class BookListCreateAPIView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


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
