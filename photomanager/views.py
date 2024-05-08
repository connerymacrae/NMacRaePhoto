from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
from django.urls import reverse
from django.urls import reverse_lazy

# Create your views here.
from .models import Photographer, Photo


def index(request):
    num_photo = Photo.objects.all().count
    num_event_photo = Photo.objects.filter(tag__exact='e').count
    num_outdoor_photo = Photo.objects.filter(tag__exact='o').count
    num_headshot_photo = Photo.objects.filter(tag__exact='h').count
    num_product_photo = Photo.objects.filter(tag__exact='p').count
    num_art_photo = Photo.objects.filter(tag__exact='a').count

    context = {
        'num_photo': num_photo,
        'num_event_photo': num_event_photo,
        'num_outdoor_photo': num_outdoor_photo,
        'num_headshot_photo': num_headshot_photo,
        'num_product_photo': num_product_photo,
        'num_art_photo': num_art_photo,
    }

    return render(request, 'index.html', context=context)


def photographer(request):
    return render(request, 'photographer_detail.html')
