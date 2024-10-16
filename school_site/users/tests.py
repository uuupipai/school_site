from django.test import TestCase
from django.contrib.auth.models import User

class UserTestCase(TestCase):
    def setUp(self):
        User.objects.create_user(username='artur_2', password='fhenhn2005')

    def test_password(self):
        user = User.objects.get(username='arr')
        self.assertTrue(user.check_password('ffff1234'))