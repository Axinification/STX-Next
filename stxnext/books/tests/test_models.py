from django.test import TestCase
from ..models import Book


class TestBook(TestCase):
    def setUp(self):
        self.book1 = Book.objects.create(
            title="Test 1"
        )

    def test_created_uncomplete_book(self):
        self.assertEquals(self.book1.external_id, None)
        self.assertEquals(self.book1.title, "Test 1")
        self.assertEquals(self.book1.authors, [])
        self.assertEquals(self.book1.published_year, '')
