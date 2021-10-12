"""
Library serializers classes.
"""

# External imports
from rest_framework import serializers

# Internal imports
from bookshelf.models import *


class AuthorSerializer(serializers.ModelSerializer):
    """
    Author serializer class.

    Defines a serializer class for author model. 
    """

    class Meta:

        model = Author
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    """
    Book serializer class.

    Defines a serializer class for book model.
    """

    authors = serializers.SlugRelatedField(queryset=Author.objects.all(), slug_field='name', many=True)
    class Meta:

        model = Book
        fields = ['id','name','publication_year','edition','authors']