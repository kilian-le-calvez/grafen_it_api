import sys
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from . import views
sys.path.append('..')
from questions import views
from videos import views

urlpatterns = [
    path('', views.getRoutes),
    path('admin/', admin.site.urls),
    path('videos/', views.getVideos),
    path('videos/create/', views.createVideo),
    path('videos/delete/', views.deleteVideo),
    path('questions/', views.getQuestions),
    path('questions/create/', views.createQuestion),
    path('questions/delete/', views.deleteQuestion),
]

urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)