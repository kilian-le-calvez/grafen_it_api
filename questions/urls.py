from django.urls import path
from . import views

urlpatterns = [
    path('videos/<str:video_id>/questions', views.getQuestions),
    path('videos/<str:video_id>/questions/create', views.createQuestion),
    path('videos/<str:video_id>/questions/delete/<str:id_question>', views.deleteQuestion),
]