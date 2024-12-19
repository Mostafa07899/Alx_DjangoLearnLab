from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import CommentViewSet, PostViewSet



router = DefaultRouter()
router.register('posts', PostViewSet, basename='post')
router.register('comments', CommentViewSet, basename='comments')

urlpatterns = [
    path('', include(router.urls)),
]