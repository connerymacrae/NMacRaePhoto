"""defines urls for accounts app"""

from django.urls import path, include, reverse_lazy
from django.contrib.auth import views as auth_views


from . import views

app_name = 'accounts'
urlpatterns = [
    # Include default auth urls
    path('', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='user-profile'),
    path('password-change/', auth_views.PasswordChangeView.as_view(success_url=reverse_lazy('accounts:password_change_done')),
         name='password_change'),
]
