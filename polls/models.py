import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


class Event(models.Model):
    date = models.DateTimeField()
    eventType = models.CharField(max_length=100)
    deck = models.CharField(max_length=100)

class Match(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    opp_deck = models.CharField(max_length=100)
    game1 = models.IntegerField(default=0)
    game2 = models.IntegerField(default=0)
    game3 = models.IntegerField(default=0)
    comment = models.CharField(max_length=100)
