from django.test import TestCase
from django.urls import reverse
from django.conf import settings


def module_url(url):
    prefix = ''

    if settings.ROOT_URLCONF != 'tasklist.urls':
        prefix = 'tasklist:'

    return url + prefix


class TasklistViewTests(TestCase):
    def test_index_view(self):
        url = module_url('index')
        response = self.client.get(reverse(url))
        self.assertEqual(response.status_code, 200)
