from django.urls import path
from . import views

urlpatterns = [
    path('videos/<str:pk>/questions', views.getQuestions),
    path('videos/<str:pk>/questions/create', views.createQuestion),
    path('videos/<str:pk>/questions/delete', views.deleteQuestion),
]