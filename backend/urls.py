from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.getRoutes),
    path('admin/', admin.site.urls),
    path('', include('videos.urls')),
    path('', include('questions.urls')),
]
