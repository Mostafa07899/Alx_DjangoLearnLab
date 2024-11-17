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
    path('admin/', views.admin_view, name='admin_view'),
    path('librarian/', views.librarian_view, name='librarian_view'),
    path('member/', views.member_view, name='member_view'),
    path('add/', views.add_book, name='add_book'),
    path('edit/', views.edit_book, name='edit_book'),
    path('delete/', views.delete_book, name='delete_book'),
]