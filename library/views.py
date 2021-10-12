"""
Library views.
"""

# External imports
from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.generics import (
    ListCreateAPIView,
    CreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework import filters

# Internal imports
from library.models import Author, Book
from library.serializers import AuthorSerializer, BookSerializer


class AuthorListCreateAPIView(ListCreateAPIView):
    """
    Author List Create Api View.

    Defines a list and create view for author model.
    """

    model = Author
    serializer_class = AuthorSerializer
    queryset = Author.objects.all().order_by('id')
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']


class AuthorRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    """
    Author Retrieve Update Destroy Api View.

    Defines a retrieve, update, destroy view for author model.
    """

    model = Author
    serializer_class = AuthorSerializer
    queryset = Author.objects.all().order_by('id')
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]


class BookListCreateAPIView(ListCreateAPIView):
    """
    Book List Create Api View.

    Defines a list and create view for author book.
    """

    model = Book
    serializer_class = BookSerializer
    queryset = Book.objects.all().order_by('id')
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['name','edition','publication_year','authors__name']
    search_fields = ['name']

class BookRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    """
    Book Retrieve Update Destroy Api View.

    Defines a retrieve, update, destroy view for book model.
    """

    model = Book
    serializer_class = BookSerializer
    queryset = Book.objects.all()


