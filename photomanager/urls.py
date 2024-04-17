from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('photographer/<int:pk>', views.PhotographerDetailView.as_view(),
         name='photographer-detail'),
]
