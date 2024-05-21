from django.db import models
from datetime import datetime, date, timedelta
from django.utils import timezone
from django.urls import reverse


# Create your models here.
class PhotoTag(models.Model):
    name = models.CharField(
        max_length=50,
        unique=True,
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('phototag-detail', args=[self.name])


class Photographer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    biography = models.TextField(max_length=1000, verbose_name="About Me")
    avatar = models.ImageField(upload_to='photos/photographers', default='photos/photos/photographers/null.png')

    def get_absolute_url(self):
        return reverse('photographer', args=[str(self.id)])

    def __str__(self):
        return f'{self.last_name}, {self.first_name}'


class Photo(models.Model):
    # id = models.IntegerField(unique=True, primary_key=True)
    date_uploaded = models.DateTimeField(default=timezone.now)
    # location = models.CharField(max_length=100)
    # photographer = models.ForeignKey('Photographer',
    #                                 on_delete=models.RESTRICT, blank=True, null=True)
    image = models.ImageField(upload_to="photos")

    '''TAGS = (
        ('e', 'Event'),
        ('w', 'Wedding'),
        ('o', 'Outdoor'),
        ('h', 'Headshot'),
        ('p', 'Product'),
        ('a', 'Art'),
    )'''

    tag = models.ManyToManyField(PhotoTag, blank=False)

    def get_absolute_url(self):
        return reverse('photo-detail', args=[str(self.id)])

    def __str__(self):
        return str(self.id)

    '''def most_recent(self):
        return self.date_uploaded >= timezone.now() - datetime.timedelta(days=30)'''
