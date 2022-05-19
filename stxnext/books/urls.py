from django.urls import path

from . import views

urlpatterns = [
    path('books/', views.BookListCreateAPIView.as_view(),
         name='book-list-post'),
    path('books/<int:pk>', views.BookRetrieveUpdateDestroyAPIView.as_view(),
         name='book-details'),
    path('import/', views.ImportAPIView.as_view(), name='import-books')
]
