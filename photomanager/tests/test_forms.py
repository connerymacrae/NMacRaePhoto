from django.test import TestCase
import datetime
from photomanager.forms import PhotoForm
from photomanager.models import Photo


class PhotoFormTest(TestCase):

    def test_form_valid(self):
        form = PhotoForm(data={
            'date_taken': datetime.date.today(),
            'location': 'Someplace',
            'tag': 'e,w,o'})
        assert form.is_valid()
        form.save()
