from django.test import TestCase
from django.urls import reverse
# Create your tests here.


class IndexViewTestCase(TestCase):

    def test_indexview(self):
        path = reverse('index')
        response = self.client.get(path)
        print(response)
