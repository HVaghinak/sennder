from django.core.cache import cache
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class GhibliTests(APITestCase):

    def test_get_ghibli_movies(self):
        """
        Ensure we can create a new account object.
        """
        url = reverse('movies')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsNotNone(cache.get(response.request['PATH_INFO']))
