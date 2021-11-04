from django.urls import path
from . import views

urlpatterns = [
    path('videos/<str:id_video>/questions', views.getQuestions),
    path('videos/<str:id_video>/questions/create', views.createQuestion),
    path('videos/<str:id_video>/questions/delete/<str:id_question>', views.deleteQuestion),
]