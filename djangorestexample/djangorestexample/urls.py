from django.urls import path
from core import views
from author.views import AuthorCreateListApi, AuthorRetriveUpdateDeleteApi
from rest_framework.authtoken.views import obtain_auth_token
from django.contrib import admin

urlpatterns = [
    path('hello/', views.HelloView.as_view(), name='hello'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('api/register/', views.UserCreate.as_view(), name="create_user"),
    path('api/login/', views.Login.as_view(), name="login"),
    path('admin/', admin.site.urls),
    path('api/blogs/', AuthorCreateListApi.as_view(), name='create-list-blog'),
    path('api/blogs/<int:pk>/', AuthorRetriveUpdateDeleteApi.as_view(), name='update-retrive-delete-blog'),
]