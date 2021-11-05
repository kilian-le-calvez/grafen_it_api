from django.urls import path
from . import views

urlpatterns = [
    path('questions/', views.getQuestions),
    path('questions/create/', views.createQuestion),
    path('questions/delete/', views.deleteQuestion),
]