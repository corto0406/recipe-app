from django.test import TestCase, Client
from django.urls import reverse

class YourViewTestCase(TestCase):
    def test_your_view(self):
        client = Client()
        response = client.get(reverse('your_url_name'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Your expected content")