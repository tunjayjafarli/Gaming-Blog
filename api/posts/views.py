from rest_framework import viewsets

from api.posts.models import Post
from api.posts.serializers import PostSerializer

# Posts API endpoints

class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    filter_fields = ('slug')
