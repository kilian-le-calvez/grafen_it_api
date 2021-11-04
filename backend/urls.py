from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.getRoutes),
    path('', include('videos.urls')),
    path('', include('questions.urls')),
]
