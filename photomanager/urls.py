from django.urls import path
from . import views

app_name = 'photomanager'
urlpatterns = [
    path('', views.index, name='index'),
    path('photographer/', views.photographer, name='photographer'),
    path('upload_photo/', views.upload_photo, name='upload_photo'),
    path('phototag/<phototag_name>', views.phototag, name='phototag'),
]
