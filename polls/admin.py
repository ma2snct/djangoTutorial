from django.contrib import admin

from .models import Event
from .models import Match

admin.site.register(Event)
admin.site.register(Match)
