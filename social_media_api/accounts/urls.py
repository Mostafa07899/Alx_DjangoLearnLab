from django.urls import path
from .views import loginView, RegisterView, ProfileView, FollowUserView, unfollowUserView


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', loginView.as_view(), name='login'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('follow/<int:user_id>/', FollowUserView.as_view(), name='follow-user'),
    path('unfollow/<int:user_id>/', unfollowUserView.as_view(), name='unfollow-user'),
]