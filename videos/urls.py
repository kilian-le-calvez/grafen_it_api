from django.urls import path
from . import views
from .. backend import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.getRoutes),
    path('videos/', views.getVideos),
    path('videos/create', views.createVideo),
    path('videos/<str:pk>/update/', views.updateVideo),
    path('videos/<str:pk>/delete/', views.deleteVideo),
    path('videos/<str:pk>/', views.getVideo),
] 

urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
