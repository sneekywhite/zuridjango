from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    author = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'blog_posts')
    created = models.DateTimeField(auto_now_add=True)
    publish = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


