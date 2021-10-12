"""
Library urls.
"""

# External imports
from django.urls import path

# Internal imports
from library.views import (
    AuthorListCreateAPIView,
    AuthorRetrieveUpdateDestroyAPIView,
    BookListCreateAPIView,
    BookRetrieveUpdateDestroyAPIView,
)


urlpatterns = [
    path('authors/', AuthorListCreateAPIView.as_view(), name='list-authors'),
    path('authors/<int:pk>/', AuthorRetrieveUpdateDestroyAPIView.as_view(), name='detail-author'),
    path('books/', BookListCreateAPIView.as_view(), name='list-books'),
    path('books/<int:pk>/', BookRetrieveUpdateDestroyAPIView.as_view(), name='detail-book'),
]