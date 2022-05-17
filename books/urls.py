from django.urls import path

from . import views

urlpatterns = [
    path('books/<int:pk>', views.BookRetrieveUpdateDestroyAPIView.as_view(),
         name='book-list'),
    path('books/', views.BookListCreateAPIView.as_view(), name='book-detail'),
    path('import/', views.ImportAPIView.as_view(), name='imported-books')
]
