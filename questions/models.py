from django.db import models

class Question(models.Model):
    #video_id = models.IntegerField(default=-1)
    author = models.TextField(default="")
    question = models.TextField(default="")
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return "Author: " + self.author + " / Question : " + self.question

    class Meta:
        ordering = ['-updated']