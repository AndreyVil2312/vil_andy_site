from django.db import models


class Question(models.Model):
    name = models.CharField(max_length=20)
    info = models.CharField(max_length=100)


class Answer(models.Model):
    text = models.CharField(max_length=500)