from django.test import TestCase, Client
from django.urls import reverse
from books.models import Book
import json


class TestBookListCreateAPIView(TestCase):
    def setUp(self):
        self.client = Client()
        self.books_url = reverse('book-list-post')
        self.book_detail_url = reverse('book-details', args=[1])

        Book.objects.create(
            id=1,
            external_id='xxxxxxxx',
            title='Księga testów',
            authors=['Axins'],
            published_year='1998',
            acquired=True,
            thumbnail='https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.capgemini.com%2Fpl-pl%2F2019%2F04%2Fan-intelligent-approach-to-continuous-testing%2F&psig=AOvVaw3ecTzpbqD9C8u7Lz31PyK7&ust=1653004947419000&source=images&cd=vfe&ved=0CAwQjRxqFwoTCKjIvsGh6vcCFQAAAAAdAAAAABAD'
        )

    def test_view_POST(self):
        response = self.client.post(self.books_url, {
            'external_id': 'xxxxxxxx',
            'title': 'Księga testów',
            'authors': ['Axins'],
            'published_year': '1998',
            'acquired': True,
            'thumbnail': 'https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.capgemini.com%2Fpl-pl%2F2019%2F04%2Fan-intelligent-approach-to-continuous-testing%2F&psig=AOvVaw3ecTzpbqD9C8u7Lz31PyK7&ust=1653004947419000&source=images&cd=vfe&ved=0CAwQjRxqFwoTCKjIvsGh6vcCFQAAAAAdAAAAABAD'
        })
        self.assertEquals(response.status_code, 201)

    def test_view_GET(self):
        response = self.client.get(self.books_url)
        self.assertEquals(response.status_code, 200)

    def test_view_detail_GET(self):
        response = self.client.get(self.book_detail_url)
        self.assertEquals(response.status_code, 200)

    def test_view_details_PATCH(self):
        response = self.client.patch(self.book_detail_url, json.dumps({
            'external_id': '!!!!!!!',
            'title': 'Księga testów',
            'authors': ['Axins'],
            'published_year': '1998',
            'acquired': True,
            'thumbnail': 'https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.capgemini.com%2Fpl-pl%2F2019%2F04%2Fan-intelligent-approach-to-continuous-testing%2F&psig=AOvVaw3ecTzpbqD9C8u7Lz31PyK7&ust=1653004947419000&source=images&cd=vfe&ved=0CAwQjRxqFwoTCKjIvsGh6vcCFQAAAAAdAAAAABAD'
        }), content_type='application/json')
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.json()['external_id'], '!!!!!!!')

    def test_view_details_DELETE(self):
        response = self.client.delete(self.book_detail_url)
        self.assertEquals(response.status_code, 204)
