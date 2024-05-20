from django.urls import path
from . import views

app_name = 'photomanager'
urlpatterns = [
    path('', views.index, name='index'),
    path('photographers/', views.photographer_detail, name='photographers'),
    path('upload_photo/', views.upload_photo, name='upload_photo'),
    path('phototags/<int:pk>', views.phototag, name='phototag'),
]
