from django.contrib import admin

from .models import Photographer, Photo, PhotoTag

# Register your models here.
admin.site.register(Photographer)
admin.site.register(Photo)
admin.site.register(PhotoTag)