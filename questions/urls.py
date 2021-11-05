from django.urls import path
from . import views

urlpatterns = [
    path('', views.getQuestions),
    path('create/', views.createQuestion),
    path('delete/', views.deleteQuestion),
]