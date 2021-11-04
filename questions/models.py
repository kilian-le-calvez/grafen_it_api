from django.db import models

class Question(models.Model):
    video_id = models.IntegerField()
    author = models.TextField()
    question = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return "Author: " + self.author + " / Question : " + self.question

    class Meta:
        ordering = ['-updated']