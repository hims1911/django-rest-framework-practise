"""djangorestexample URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from core import views
from author.views import AuthorCreateListApi, AuthorRetriveUpdateDeleteApi
from rest_framework.authtoken.views import obtain_auth_token
from django.contrib import admin

urlpatterns = [
    path('hello/', views.HelloView.as_view(), name='hello'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('api/create-user/', views.UserCreate.as_view(), name="create_user"),
    path('api/login', views.login, name="login"),
    path('admin/', admin.site.urls),
    path('api/blogs/', AuthorCreateListApi.as_view(), name='create-list-blog'),
    path('api/blogs/<int:pk>/', AuthorRetriveUpdateDeleteApi.as_view(), name='update-retrive-delete-blog'),
]