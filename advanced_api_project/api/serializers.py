from rest_framework import serializers
from .models import Author, Book
from datetime import datetime



class BookSerializer(serializers.ModelSerializer):
     """
    Serializer for the Book model.

    Fields:
        - id (Read-Only): The unique ID of the book.
        - title: The title of the book.
        - publication_year: The year the book was published.
        - author: The ID of the author who wrote the book.
    Validation:
        - publication_year: Ensures the year is not in the future.
    """
     class Meta:
        model = Book
        fields = ['id','title','pyblication_year','author']

     def validate_publication_year(self, value):
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError("The publication year cannot be in the future.")
        return value
    

class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializer for the Author model.

    Fields:
        - id (Read-Only): The unique ID of the author.
        - name: The name of the author.
        - books: A nested representation of books written by the author.
    Nested Serialization:
        - Uses BookSerializer to serialize the related books dynamically.
        - Read-only to prevent modification of books through the AuthorSerializer.
    """
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id','name','books']