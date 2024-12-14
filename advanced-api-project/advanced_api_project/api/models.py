from django.db import models

# Create your models here.

from django.db import models

class Author(models.Model):
   """
    The Author model represents authors who have written books.
    
    Fields:
        - name (CharField): The name of the author, with a max length of 255 characters.
    Relationships:
        - One-to-Many: An author can have multiple books (related_name='books').
    """
    name = models.CharField(max_length=255)

     def __str__(self):
        return self.name


class Book(models.Model):
"""
    The Book model represents books authored by an Author.

    Fields:
        - title (CharField): The title of the book.
        - publication_year (IntegerField): The year the book was published.
        - author (ForeignKey): A foreign key linking to the Author model.
    Relationships:
        - Many-to-One: Each book is associated with one author (on_delete=models.CASCADE).
    """
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return f"{self.title} ({self.publication_year})"
