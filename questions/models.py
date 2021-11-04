from django.db import models
from django.utils import timezone

import datetime
import sys

from videos.views import updateVideo
sys.path.append("..")
from videos.models import Video

class Question(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    author = models.TextField()
    question = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return "Author: " + self.author + " / Question : " + self.question

    class Meta:
        ordering = ['-updated']