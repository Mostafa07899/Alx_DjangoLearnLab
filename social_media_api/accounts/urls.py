from django.urls import path
from .views import loginView, RegisterView, ProfileView


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', loginView.as_view(), name='login'),
    path('profile/', ProfileView.as_view(), name='profile'),
]