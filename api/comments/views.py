from rest_framework import viewsets

from api.comments.models import Comment
from api.comments.serializers import CommentSerializer

# Comments API endpoints

class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    filter_fields = ('post',)

