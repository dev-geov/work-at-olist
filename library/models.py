"""
Library models.
"""

# External imports
from django.db import models


class Author(models.Model):
    """
    Author class.

    Defines a model for author data.
    """

    name = models.CharField(max_length=50, null=False, unique=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    """
    Book class.

    Defines a model for book data.
    """

    name = models.CharField(max_length=50)
    edition = models.CharField(max_length=50)
    publication_year = models.IntegerField()
    authors = models.ManyToManyField(Author, related_name='books')

