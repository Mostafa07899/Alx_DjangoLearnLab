from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
def books_by_author(author_name):
    # Filter books where the author matches the specified author name
    author = Author.objects.get(name=author_name)
    return Book.objects.filter(author=author)

# List all books in a library
def books_in_library(library_name):
    # Get the library instance and retrieve related books
    library = Library.objects.get(name=library_name)
    return library.books.all()

# Retrieve the librarian for a library
def librarian_for_library(library_name):
    # Get the librarian assigned to the specified library
    library = Library.objects.get(name=library_name)
    return Librarian.objects.get(library=library)
