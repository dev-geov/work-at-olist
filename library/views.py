"""
Library views.
"""

# External imports

from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBacken

from rest_framework.generics import (
    ListCreateAPIView,
    CreateAPIView,
    RetrieveUpdateDestroyAPIViewd,
)
from rest_framework import filters

# Internal imports
from bookshelf.models import Author, Book
from bookshelf.serializers import AuthorSerializer, BookSerializer


class AuthorListCreateAPIView(ListCreateAPIView):

    model = Author
    serializer_class = AuthorSerializer
    queryset = Author.objects.all().order_by('id')
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']


class AuthorRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):

    model = Author
    serializer_class = AuthorSerializer
    queryset = Author.objects.all().order_by('id')
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]


class BookListCreateAPIView(ListCreateAPIView):

    model = Book
    serializer_class = BookSerializer
    queryset = Book.objects.all().order_by('id')
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['name','edition','publication_year','authors__name']
    search_fields = ['name']

class BookRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):

    model = Book
    serializer_class = BookSerializer
    queryset = Book.objects.all()


