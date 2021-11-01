from django.db import models

class Video(models.Model):
    title = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title[0:50]
    
    class Meta:
        ordering = ['-updated']