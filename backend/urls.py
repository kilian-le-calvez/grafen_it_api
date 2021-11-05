import sys
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from . import views
sys.path.append('..')
from questions import views as questionsViews
from videos import views as videosViews

urlpatterns = [
    path('', views.getRoutes),
    path('admin/', admin.site.urls),
    path('videos/', videosViews.getVideos),
    path('videos/create/', videosViews.createVideo),
    path('videos/delete/', videosViews.deleteVideo),
    static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT),
    path('questions/', questionsViews.getQuestions),
    path('questions/create/', questionsViews.createQuestion),
    path('questions/delete/', questionsViews.deleteQuestion),
]