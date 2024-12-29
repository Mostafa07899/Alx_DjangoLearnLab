from django.shortcuts import render
from django.contrib.contenttypes.models import ContentType
from rest_framework import viewsets, permissions, status, generics
from .models import Post, Comment, Like
from notifications.models import Notification
from .serializers import PostSerializer, CommentSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

# Create your views here.


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        queryset = super().get_queryset()
        title = self.request.query_params.get('title', None)
        content = self.request.query_params.get('content', None)
        if title:
            queryset = queryset.filter(title__icontains=title)
        if content:
            queryset = queryset.filter(title__icontains=content)
        return queryset
    

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)



class FeedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        following_users = request.user.following.all()
        posts = Post.objects.filter(author__in=following_users).order_by('-created_at')
        feed_data = [{'title': post.title, 'content': post.content, 'author': post.author.username} for post in posts]
        return Response(feed_data, status=status.HTTP_200_OK)



class LikePostView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        try:
            post = Post.objects.get(pk)
            like, created = Like.objects.get_or_create(user=request.user, post=post)

            if not created:
                return Response({'error': 'you have already like this post'}, status=status.HTTP_400_BAD_REQUEST)
            

            Notification.objects.create(
                recipient=post.author,
                actor=request.user,
                verb='like your post',
                target=post, 
            )
            return Response({'detail': 'post like successfully'}, status=status.HTTP_200_OK)
        except post.DoesNotExist:
            return Response({'error': 'post not found'}, status=status.HTTP_404_NOT_FOUND)


class UnlikePostView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        try:
            post = Post.objects.get(pk=pk)
            like = Like.objects.filter(user=request.user, post=post)

            if like.exists():
                like.delete()
                return Response({'detail': 'post unlike successfully'}, status=status.HTTP_200_OK)

            return Response({'error': 'you did not like thi post'}, status=status.HTTP_400_BAD_REQUEST)
        except post.DoesNotExist:
            return Response({'error': 'post not found'}, status=status.HTTP_404_NOT_FOUND)  