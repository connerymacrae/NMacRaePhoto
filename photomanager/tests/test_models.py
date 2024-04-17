from django.test import TestCase

from photomanager.models import Photo, Photographer


class PhotographerModelTest(TestCase):
    def setUp(self):
        Photographer.objects.create(first_name='John', last_name='Doe', biography='I love')

    def test_first_name_label(self):
        photographer = Photographer.objects.get(id=1)
        field_label = photographer._meta.get_field('first_name').verbose_name
        self.assertEqual(field_label, 'first name')

    def test_last_name_label(self):
        photographer = Photographer.objects.get(id=1)
        field_label = photographer._meta.get_field('last_name').verbose_name
        self.assertEqual(field_label, 'last name')

    def test_biography_label(self):
        photographer = Photographer.objects.get(id=1)
        field_label = photographer._meta.get_field('biography').verbose_name
        self.assertEqual(field_label, 'About Me')

    def test_first_name_max_length(self):
        photographer = Photographer.objects.get(id=1)
        max_length = photographer._meta.get_field('first_name').max_length
        self.assertEqual(max_length, 100)

    def test_last_name_max_length(self):
        photographer = Photographer.objects.get(id=1)
        max_length = photographer._meta.get_field('last_name').max_length
        self.assertEqual(max_length, 100)

    def test_biography_max_length(self):
        photographer = Photographer.objects.get(id=1)
        max_length = photographer._meta.get_field('biography').max_length
        self.assertEqual(max_length, 1000)

