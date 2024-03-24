from django.test import TestCase
from .models import YourModel

class YourModelTestCase(TestCase):
    def setUp(self):
        YourModel.objects.create(name="Test Recipe", description="Test Description")

    def test_model_creation(self):
        obj = YourModel.objects.get(name="Test Recipe")
        self.assertEqual(obj.name, "Test Recipe")
        self.assertEqual(obj.description, "Test Description")
