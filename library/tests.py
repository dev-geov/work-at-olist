"""
Library tests.
"""

# External imports
from django.test import TestCase
from django.urls import reverse

from rest_framework.test import APITestCase
from rest_framework import status

# Internal imports
from library.models import Author, Book


class AuthorTests(APITestCase):
    """
    Author Test class.

    Defines tests for author endpoints.
    """

    def test_endpoint_create_author(self):
        """
        Test author create endpoint.
        """

        url = reverse('list-authors')
        data = {'name': 'Geovani Silva'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_endpoint_list_authors(self):
        """
        Test authors list endpoint.
        """

        url = reverse('list-authors')
        list_authors = [
            {'name':'Geovani Silva'},
            {'name': 'Barbara Silva'},
            {'name': 'Borges pinscher'}
        ]
        for data in list_authors:
            author, created = Author.objects.get_or_create(name=data['name'])
        response = self.client.get(url, format='json')
        
        expected_total = len(response.data.get('results'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Author.objects.count(), expected_total)
    
    def test_endpoint_detail_author(self):
        """
        Test author retrieve endpoint.
        """

        author, created = Author.objects.get_or_create(name='Geo')
        url = reverse('detail-author', kwargs={'pk': author.pk})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_endpoint_update_author(self):
        """
        Test author update endpoint.
        """

        author, created = Author.objects.get_or_create(name='Geovani')
        url = reverse('detail-author', kwargs={'pk': author.pk})
        data = {
            'name': 'Silva'
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Author.objects.get().name, 'Silva')
    
    def test_endpoint_delete_author(self):
        """
        Test author delete endpoint.
        """

        author, created = Author.objects.get_or_create(name='Geovani')
        url = reverse('detail-author', kwargs={'pk': author.pk})

        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class BookTests(APITestCase):
    """
    Book Test class.

    Defines tests for book endpoints.
    """

    def test_endpoint_create_book(self):
        """
        Test book create endpoint.
        """

        url = reverse('list-books')

        author, created = Author.objects.get_or_create(name='Geovani')
        data = {
            'name': 'Python rest api',
            'edition': '3th',
            'publication_year': 2009,
            'authors': [author.name],
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_endpoint_list_books(self):
        """
        Test books list endpoint.
        """

        url = reverse('list-books')
        author, created = Author.objects.get_or_create(name='Geovani')
        list_books = [
            {
                'name':'Modeling data api',
                'edition': '1st',
                'publication_year': 2021,
            },
            {
                'name': 'Git for beginners',
                'edition': '2nd',
                'publication_year': 2020,

            },
            {
                'name': 'Soft skills',
                'edition': '1st',
                'publication_year': 2020,
            }
        ]
        for data in list_books:
            book = Book(**data)
            book.save()
            book.authors.add(author)
        response = self.client.get(url, format='json')
        
        expected_total = len(response.data.get('results'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Book.objects.count(), expected_total)
    
    def test_endpoint_detail_book(self):
        """
        Test book retrieve endpoint.
        """

        author, created = Author.objects.get_or_create(name='Geo')
        book_data = {
            'name': 'Soft skills',
            'edition': '1st',
            'publication_year': 2020,
        }
        book = Book(**book_data)
        book.save()
        book.authors.add(author)
        url = reverse('detail-book', kwargs={'pk': book.pk})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_endpoint_update_book(self):
        """
        Test book update endpoint.
        """

        author, created = Author.objects.get_or_create(name='Geovani')
        book_data = {
            'name': 'Soft skills',
            'edition': '1st',
            'publication_year': 2020,
        }
        book = Book(**book_data)
        book.save()
        book.authors.add(author)
        url = reverse('detail-book', kwargs={'pk': book.pk})
        data = {
            'name': 'Soft skill for dummies'
        }
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Book.objects.get().name, data.get('name'))
    
    def test_endpoint_delete_author(self):
        """
        Test book delete endpoint.
        """

        author, created = Author.objects.get_or_create(name='Geovani')
        book_data = {
            'name': 'Soft skills',
            'edition': '1st',
            'publication_year': 2020,
        }
        book = Book(**book_data)
        book.save()
        book.authors.add(author)
        url = reverse('detail-book', kwargs={'pk': book.pk})

        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)