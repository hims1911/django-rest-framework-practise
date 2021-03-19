from django.db import models
from core.models import User

class AuthorBlog(models.Model):
    artist = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    body = models.CharField(max_length=30)
    summary = models.CharField(max_length=60)
    created_at = models.DateTimeField(auto_now=True)