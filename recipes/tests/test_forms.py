from django.test import TestCase
from .forms import YourForm

class YourFormTestCase(TestCase):
    def test_valid_form(self):
        data = {'name': 'Test Recipe', 'description': 'Test Description'}
        form = YourForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        data = {'name': '', 'description': 'Test Description'}
        form = YourForm(data=data)
        self.assertFalse(form.is_valid())
