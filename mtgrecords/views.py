from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.http import HttpResponse
from twitter import *
from . import api

from .models import Event, Match


class IndexView(generic.ListView):
    template_name = 'mtgrecords/index.html'
    context_object_name = 'latest_event_list'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(
            date__lte=timezone.now()
        ).order_by('-date')[:5]


class DetailView(generic.DetailView):
    model = Event
    template_name = 'mtgrecords/detail.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Event.objects.filter(date__lte=timezone.now())

class TweetView(generic.TemplateView):
    template_name = "mtgrecords/tweet.html"

    t = Twitter(
        auth=OAuth(api.token, api.token_secret, api.consumer_key, api.consumer_secret))

    # Get your "home" timeline
    print(t.statuses.home_timeline())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['event'] = "draft"
        return context
