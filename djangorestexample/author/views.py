from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from .serializers import AuthorSerializer
from .models import AuthorBlog

""" API to create a Author Blog """
class AuthorApi(generics.CreateAPIView):
    queryset = AuthorBlog.objects.all()
    serializer_class = AuthorSerializer

""" API to show all the authors and their respective blogs """
class AllAuthorApi(generics.ListAPIView):
    queryset = AuthorBlog.objects.all()
    serializer_class = AuthorSerializer

""" API to update the author view by their ID """
class AuthorUpdateApi(generics.RetrieveUpdateAPIView):
    queryset = AuthorBlog.objects.all()
    serializer_class = AuthorSerializer

""" API to delete the author blog by their ID """
class AuthorDeleteApi(generics.DestroyAPIView):
    queryset = AuthorBlog.objects.all()
    serializer_class = AuthorSerializer

