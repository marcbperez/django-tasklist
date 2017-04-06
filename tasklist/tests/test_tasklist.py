from django.test import TestCase
from django.urls import reverse
from django.conf import settings


class TasklistViewTests(TestCase):
    url_prefix = "" if settings.ROOT_URLCONF == "tasklist.urls" else "tasklist:"

    def test_index_view(self):
        response = self.client.get(reverse(self.url_prefix + 'index'))
        self.assertEqual(response.status_code, 200)
