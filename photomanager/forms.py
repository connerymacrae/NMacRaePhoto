from django import forms

from photomanager.models import Photo


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['date_taken', 'location', 'image', 'tag']
