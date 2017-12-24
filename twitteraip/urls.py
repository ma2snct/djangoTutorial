import django.contrib.auth.views

urlpatterns = [
    :
    url(r'^login/$',
        django.contrib.auth.views.login,
        {
            'template_name': 'twitterapi/login.html',
        },
        name='login'),
    url(r'^logout/$',
        django.contrib.auth.views.logout,
        {
            'template_name': 'twitterapi/logout.html',
        },
        name='logout'),
]
