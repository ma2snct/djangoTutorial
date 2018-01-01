from django.urls import path
from . import views
from django.conf.urls import url, include
from django.conf import settings

app_name = 'mtgrecords'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/tweet/', views.TweetView.as_view(), name='tweet'),
]
