from rest_framework import  serializers
from .models import AuthorBlog

class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = AuthorBlog
        fields = '__all__'