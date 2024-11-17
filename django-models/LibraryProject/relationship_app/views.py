from django.shortcuts import render, get_object_or_404
from django.views.generic.detail import DetailView
from .models import Book
from .models import Library
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect
from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse
from django.http import HttpResponseForbidden 
from .models import UserProfile
from django.contrib.auth.decorators import permission_required

# Create your views here.

def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

class LibraryDetailView(DetailView):
    model = Library 
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("login")
    else:
        form = UserCreationForm()
        return render(request, "register.html", {"form": form})
    

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "register.html"

class CustomLoginView(LoginView):
    template_name = 'login.html'

class CustomLogoutView(LogoutView):
    template_name = 'logout.html'



LoginView = auth_views.LoginView.as_view(template_name="login.html")
LogoutView = auth_views.LogoutView.as_view(template_name="logut.html")


def is_admin(user):
    return user.userprofile.role == 'Admin'

def is_librarian(user):
    return user.userprofile.role == 'Librarian'

def is_member(user):
    return user.userprofile.role == 'Member'



def admin_view(request):
    return HttpResponse("Welcome to the Admin dashboard.")

def member_view(request):
    return HttpResponse("Welcome to the Member dashboard.")

def librarian_view(request):
    return HttpResponse("Welcome to the Librarian dashboard.")


@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    return HttpResponse("Book added successfully.")

@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request):
    book = get_object_or_404(Book)
    return HttpResponse("Book edited successfully.")

@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request):
    return HttpResponse("Book deleted successfully.")
