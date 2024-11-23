from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import permission_required
from .models import Book
from django.http import HttpResponse


# Create your views here.

@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    # Logic for viewing items
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

@permission_required('bookshelf.can_create', raise_exception=True)
def book_create(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        Book.objects.create(title=title, content=content)
        return HttpResponse("Book created successfully!")
    return render(request, 'books/book_form.html')


@permission_required('bookshelf.can_edit', raise_exception=True)
def book_edit(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        book.title = request.POST.get("title")
        book.content = request.POST.get("content")
        book.save()
        return HttpResponse("Book updated successfully!")
    return render(request, 'books/book_form.html',{'book': book})


def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book.delete()
    return HttpResponse("Book deleted successfully!")