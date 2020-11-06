from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, RequestsClient, APITestCase
from books.models import *

class BookTests(APITestCase):

    def test_create_book(self):
        """
        Ensure we can create a new book object.
        """
        # url = reverse('BookListView')
        client = APIClient()
        data =  {
            "title": "Django APIs",
            "author": 5,
            "category": "AVTRE",
            "format": "HD-CVR",
            "year": 2009,
            "price": "40.00",
        }
        self.client.post('/admin/books/', data, format='json')
        # response = self.client.post(url, data, format='json')
        # self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # self.assertEqual(Book.objects.count(), 1)
        # self.assertEqual(Book.objects.get().title, "Django APIs")
    
    def test_get_books(self):

        client = RequestsClient()
        response = client.get('http://127.0.0.1:8000/api/v1/books/')
        self.assertEqual(response.status_code, 200)

