# recipes/tests/test_views.py

from django.test import TestCase
from django.urls import reverse

class StaticFilesTest(TestCase):
    def test_static_files_exist(self):
        response = self.client.get(reverse('home'))

        image_url = reverse('static', args=['static/recipe_images/image.jpg'])

        self.assertEqual(response.status_code, 200)

        self.assertContains(response, 'src="{0}"'.format(image_url))

# Add more tests as needed for other static files and views
