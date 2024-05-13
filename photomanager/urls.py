from django.urls import path
from . import views

app_name = 'photomanager'
urlpatterns = [
    path('', views.index, name='index'),
    path('photographer/', views.photographer, name='photographer'),
]
