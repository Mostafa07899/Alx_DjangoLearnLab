from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Book
from .models import Library
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

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
            return redirect("home")
    else:
        form = UserCreationForm()
        return render(request, "register.html", {"form": form})
    

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "register.html"
    

LoginView = auth_views.LoginView.as_view(template_name="login.html")
LogoutView = auth_views.LogoutView.as_view(template_name="logut.html")
