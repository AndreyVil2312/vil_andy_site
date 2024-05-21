from django.db import models


class Question(models.Model):
    name = models.CharField(max_length=20, null=False, default='Name')
    info = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Answer(models.Model):
    question_name = models.CharField(max_length=20, null=False, default="Question name")
    text = models.CharField(max_length=500)
