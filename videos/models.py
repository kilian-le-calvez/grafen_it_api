from django.db import models

class Video(models.Model):
    title = models.TextField()
    videofile = models.FileField(upload_to='media/%y', null=True, verbose_name="")
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Title: " + self.title[0:50] + "  /  Videofile: " + str(self.videofile)[0:50]
    
    class Meta:
        ordering = ['-updated']

