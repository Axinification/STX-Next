from django.test import SimpleTestCase
from books.views import (BookRetrieveUpdateDestroyAPIView,
                         BookListCreateAPIView, ImportAPIView)
from django.urls import resolve, reverse


class TestUrls(SimpleTestCase):
    def test_list_url_is_resolved(self):
        url = reverse('book-list-post')
        self.assertEquals(
            resolve(url).func.view_class, BookListCreateAPIView)

    def test_details_url_is_resolved(self):
        url = reverse('book-details', args=[1])
        self.assertEquals(
            resolve(url).func.view_class, BookRetrieveUpdateDestroyAPIView)

    def test_import_url_is_resolved(self):
        url = reverse('import-books')
        self.assertEquals(resolve(url).func.view_class, ImportAPIView)
