from django.test import TestCase
from .models import Bread
from django.contrib.auth import get_user_model

# Create your tests here.
class TestBread(TestCase):
    def test_name(self):
        name = get_user_model().objects.create_user(
            name="Daves Killer Bread",
            description='nine grain oats',
            bread_type='wheat'
        )
        self.assertIsInstance(name, Bread)
        self.assertEqual(name.bread_type, 'wheat')
        