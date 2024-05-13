from django.test import TestCase
from accounts.forms import UserRegisterForm
from django.urls import reverse, resolve
from django.contrib.auth import get_user_model
User = get_user_model()


class RegisterUserTests(TestCase):

    def test_register_view(self):
        # make sure that user registration form exists
        response = self.client.get('/accounts/register/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/register.html')

    def test_register_form(self):
        # define data to be passed to UserCreationForm
        data = {'username': 'test',
                'email': 'john@john.com',
                'password1': 'XD78xd87!',
                'password2': 'XD78xd87!'}
        # post data to form
        response = self.client.post('/accounts/register/', data=data)
        # data has been passed and user created, redirect to login page
        self.assertEqual(response.status_code, 302)
        created_user = User.objects.get(username='test')
        self.assertEqual(created_user.email, 'john@john.com')
        self.assertRedirects(response, "/photomanager/")
        #self.assertTemplateUsed(follow_on_response, 'photomanager:index')


# class AccountsTest(TestCase):
