from django.shortcuts import render
from django.core.exceptions import PermissionDenied
from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import AuthorSerializer
from .models import AuthorBlog

""" API to create a Author Blog """
class AuthorCreateListApi(generics.CreateAPIView, generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = AuthorBlog.objects.all()
    serializer_class = AuthorSerializer

    def get_queryset(self):
        queryset = self.queryset.all()
        user_id = self.request.user.id
        title = self.request.query_params.get('title', None)
        summary = self.request.query_params.get('summary', None)
        
        if self.request.user.is_superuser:
            pass
        elif user_id:
            queryset = queryset.filter(artist_id=user_id)
        if title:
            queryset = queryset.filter(title__contains=title)
        if summary:
            queryset = queryset.filter(summary__contains=summary)
    
        return queryset
    
    def post(self, request, *args, **kwargs):
        body_id = request.data.get('artist', None)
        if(body_id):
            body_id = int(body_id)
            if((request.user.id == body_id) or request.user.is_superuser):
                return generics.CreateAPIView.post(self,request, *args, **kwargs)
            else:
                return Response("You cannot create blog for other person", status=400)
        else:
            return Response("Please enter valid artist id")

""" API to update,delete the author view by their ID """
class AuthorRetriveUpdateDeleteApi(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = AuthorBlog.objects.all()
    serializer_class = AuthorSerializer

    def get_queryset(self):
        queryset = self.queryset.all()
        user_id = self.request.user.id

        if self.request.user.is_superuser:
            pass
        elif user_id:
            queryset = queryset.filter(artist_id=user_id)
    
        return queryset



