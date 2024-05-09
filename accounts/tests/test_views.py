from django.test import TestCase
from django.contrib.auth import get_user_model
User = get_user_model()

class AccountsViewTests(TestCase):

    def test_login_button_appears_on_homepage(self):

    def test_login_button_redirects_to_login_page(self):

    def test_user_can_login(self):
        """should I test the redirect to home here
        or should it be a separate test?"""

    def test_welcome_message_is_displayed(self):

    def test_logout_button_is_displayed(self):
        """same question about the redirect after logout"""



