from django.contrib.auth.models import User
from django.db import models


class Survey(models.Model):

    title = models.CharField(max_length=64)
    participant = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Question(models.Model):

    survey = models.ForeignKey(Survey, on_delete=models.CASCADE, related_name='questions', null=True)
    question = models.CharField(max_length=300)

    def __str__(self):
        return self.question


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices', null=True)
    option = models.CharField(max_length=150)
    vote = models.IntegerField(default=0)

    def __str__(self):
        return self.option


class Subchoice(models.Model):

    suboption = models.ForeignKey(Choice, on_delete=models.CASCADE, related_name='subchoices', max_length=150)
    subtext = models.CharField(max_length=150, null=True)
    vote = models.IntegerField(default=0)

    def __str__(self):
        return self.subtext

