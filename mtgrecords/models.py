from django.db import models

class Event(models.Model):
    date = models.DateTimeField()
    event_type = models.CharField(max_length=100)
    deck = models.CharField(max_length=100)

    def __str__(self):
        return self.date.strftime('%m/%d') + " " + self.event_type

class Match(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    opp_deck = models.CharField(max_length=100)
    game1 = models.IntegerField(default=0)
    game2 = models.IntegerField(default=0)
    game3 = models.IntegerField(default=0)
    comment = models.CharField(max_length=100)

    def __str__(self):
        return self.opp_deck
