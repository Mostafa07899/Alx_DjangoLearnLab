# Delete a Book Instance

In this operation, we will delete the book instance that we created earlier. To do this, we first need to import the `Book` model from our `bookshelf` app.

```python
# Import the Book model
from bookshelf.models import Book

# Retrieve the book instance to be deleted
book_to_delete = Book.objects.get(title="1984")

# Delete the book instance
book.delete()
