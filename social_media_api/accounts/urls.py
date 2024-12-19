from django.urls import path
from .views import loginView, RegisterView


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', loginView.as_view(), name='login'),
]