from django.test import TestCase

from .models import User

class UserModelTests(TestCase):

    def test_is_premium_default(self):
        user = User()
        self.assertFalse(user.is_premium())

    def test_is_premium_when_premium(self):
        user = User(role=User.Role.PREMIUM)
        self.assertTrue(user.is_premium())
