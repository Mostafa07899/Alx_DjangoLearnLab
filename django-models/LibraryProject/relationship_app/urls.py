from django.urls import path
from . import views
from .views import list_books
from django.contrib.auth.views import LoginView, LogoutView



urlpatterns = [
    path('books/', views.list_books, name='list_books'),
    path('library/<int:pk>', views.LibraryDetailView.as_view(), name='library_detail'),   
    path("login/", LoginView.as_view(template_name='registration/login.html'), name="login"),
    path("logut/", LogoutView.as_view(template_name='registration/logout.html'), name="logout"),
    path("register/", views.register, name="register"),
]