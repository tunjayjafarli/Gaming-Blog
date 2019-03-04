from django.db import models
from django.utils.text import slugify

from api.users.models import User


class Post(models.Model):
    """
    Database model for blog posts.
    """
    title = models.CharField(max_length=255, unique=True, blank=False)
    article = models.TextField(blank=True)
    author = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=255, unique=True, blank=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

