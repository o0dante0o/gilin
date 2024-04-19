from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Country

class CountryTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_add_country(self):
        url = reverse('add-country')  # Asegúrate de tener una URL nombrada 'add_country' en tus urls.py
        data = {'name': 'Test Country', 'phone_code': 123}
        
        # Test para caso exitoso
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Country.objects.count(), 1)
        self.assertEqual(Country.objects.get().name, 'Test Country')

        # Test para caso de error (por ejemplo, datos incompletos)
        data_incomplete = {'name': 'Incomplete Country'}
        response = self.client.post(url, data_incomplete, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)