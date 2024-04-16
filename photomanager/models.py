from django.db import models
import datetime
from django.utils import timezone
from django.urls import reverse


# Create your models here.


class Photographer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    biography = models.TextField(max_length=1000)

    def get_absolute_url(self):
        return reverse('photographer-detail', args=[str(self.id)])

    def __str__(self):
        return f'{self.last_name}, {self.first_name}'


class Photo(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    date_taken = models.DateTimeField(null=True, blank=True)
    location = models.CharField(max_length=100)
    photographer = models.ForeignKey('Photographer',
                                     on_delete=models.RESTRICT)
    image = models.ImageField(upload_to="photos")

    TAGS = (
        ('e', 'Event'),
        ('w', 'Wedding'),
        ('o', 'Outdoor'),
        ('h', 'Headshot'),
        ('p', 'Product'),
        ('a', 'Art'),
    )

    tag = models.CharField(max_length=6, choices=TAGS, blank=True)

    def get_absolute_url(self):
        return reverse('photo-detail', args=[str(self.id)])

    def __str__(self):
        return f'{self.location} - {str(self.id)}'

    def most_recent(self):
        return self.date_taken >= timezone.now() - datetime.timedelta(days=30)

