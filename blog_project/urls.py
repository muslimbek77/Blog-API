# blog_project/urls.py
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
path('admin/', admin.site.urls),
path('api/v1/', include('posts.urls'),name = 'api'),
path('api-auth/', include('rest_framework.urls')),
path('api/v1/rest-auth/', include('rest_auth.urls')),
    ]