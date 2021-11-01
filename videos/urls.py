from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes),
    path('videos/', views.getVideos),
    path('videos/create', views.createVideo),
    path('videos/<str:pk>/update/', views.updateVideo),
    path('videos/<str:pk>/delete/', views.deleteVideo),
    path('videos/<str:pk>/', views.getVideo),
]