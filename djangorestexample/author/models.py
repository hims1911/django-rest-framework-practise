from django.db import models
from core.models import User
from django.core.validators import FileExtensionValidator
from core.models import User

def directoy_path(instace, filename):
    return '{0}/{1}'.format("document", filename)

class AuthorBlog(models.Model):
    artist = models.ForeignKey(User, on_delete=models.CASCADE, null = False)
    title = models.CharField(max_length=30, null = False)
    body = models.CharField(max_length=30, null = False)
    summary = models.CharField(max_length=60, null = False)
    created_at = models.DateTimeField(auto_now=True)
    document = models.FileField(upload_to = directoy_path, validators=[FileExtensionValidator(allowed_extensions=['pdf'])], null=True)