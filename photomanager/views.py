from django.shortcuts import render, redirect
from django.views import generic
from django.http import HttpResponse
from django.urls import reverse
from django.urls import reverse_lazy

# Create your views here.
from .models import Photographer, Photo, PhotoTag
from .forms import PhotoForm


def index(request):
    phototags = PhotoTag.objects.all()
    num_photo = Photo.objects.all().count
    num_event_photo = PhotoTag.objects.filter(name__exact='Event').count
    num_outdoor_photo = PhotoTag.objects.filter(name__exact='outdoor').count
    num_headshot_photo = PhotoTag.objects.filter(name__exact='headshot').count
    num_product_photo = PhotoTag.objects.filter(name__exact='product').count
    num_art_photo = PhotoTag.objects.filter(name__exact='art').count

    context = {
        'phototags': phototags,
        'num_photo': num_photo,
        'num_event_photo': num_event_photo,
        'num_outdoor_photo': num_outdoor_photo,
        'num_headshot_photo': num_headshot_photo,
        'num_product_photo': num_product_photo,
        'num_art_photo': num_art_photo,
    }

    return render(request, 'index.html', context)


def photographer_detail(request):
    photographers = Photographer.objects.order_by('last_name')
    phototags = PhotoTag.objects.all()
    context = {'photographers': photographers, 'phototags': phototags}
    return render(request, 'photomanager/photographers.html', context=context)


'''class PhotographerListView(generic.ListView):
    model = Photographer'''


def upload_photo(request):
    if request.method != 'POST':
        # no data submitted, create new form
        form = PhotoForm()
    else:
        # POST data submitted; process data
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('photomanager:upload_photo')

    # Display a blank or invalid form
    context = {'form': form}
    return render(request, 'photomanager/upload_photo.html', context)


def phototag(request, pk):
    phototags = PhotoTag.objects.get(pk),
    photos = Photo.objects.filter(phototag=phototag_name).order_by('-date_uploaded')
    context = {'phototags': phototags, 'photos': photos}
    return render(request, 'photomanager/phototag.html', context)
