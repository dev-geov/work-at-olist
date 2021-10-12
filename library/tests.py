"""
Library tests.
"""

# External imports
from django.test import TestCase
from django.urls import reverse

from rest_framework.test import APITestCase
from rest_framework import status

# Internal imports
from library.models import Author


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