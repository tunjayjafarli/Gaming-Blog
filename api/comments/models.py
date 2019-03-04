from django.db import models

from api.posts.models import Post
from api.users.models import User

class Comment(models.Model):
	"""
	Database model for comments on blog posts.
	"""
	text = models.TextField()
	created = models.DateTimeField(auto_now_add=True)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	post = models.ForeignKey(Post, on_delete=models.CASCADE)

	class Meta:
		ordering = ['-created']

	def __str__(self):
		return self.text