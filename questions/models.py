from django.db import models
from django.utils import timezone

import datetime

from videos.views import updateVideo

class Question(models.Model):
    author = models.CharField(max_length=1000)
    question = models.CharField(max_length=1000)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return "Author: " + self.author + " / Question : " + self.question

    class Meta:
        ordering = ['-updated']