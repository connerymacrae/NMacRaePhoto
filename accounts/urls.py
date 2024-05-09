'''defines urls for accounts app'''

from django.urls import path, include

app_name = 'accounts'
urlpatterns = [
    # Include default auth urls
    path('', include('django.contrib.auth.urls')),
]