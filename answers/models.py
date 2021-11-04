from django.db import models
from .. questions.models import Question

class Answer(models.Model):
    models.ForeignKey(Question, ...) # relation plurials to one 
    on_delete=models.CASCADE # delete Answer associated to a deleted Question
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=1000)

    def __str__(self):
        return self.answer_text
