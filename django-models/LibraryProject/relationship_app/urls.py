from django.urls import path
from . import views
from .views import list_books
from .views import LoginView, LogoutView, register



urlpatterns = [
    path('books/', views.list_books, name='list_books'),
    path('library/<int:pk>', views.LibraryDetailView.as_view(), name='library_detail'),   
    path("login/", LoginView, name="login"),
    path("logut/", LogoutView, name="logout"),
    path("register/", views.SignUpView.as_view(), name="register"),
]