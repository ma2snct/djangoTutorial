from django.urls import path

from . import views

from django.conf.urls import url, include
from django.conf import settings
from .views import ApiEndpoint

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('login', views.login, name='login'),
    path('logout', views.logout_view, name='logout'),
]
