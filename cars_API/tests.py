from django.test import TestCase
from django.contrib.auth.models import User
from .models import Car
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse

# Model Test Case
class CarModelTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username='testuser', password='12345')
        cls.car = Car.objects.create(
            model='Model S',
            brand='Tesla',
            price='79999.99',
            is_bought=True,
            buyer=cls.user,
            buy_time='2023-01-01T12:00:00Z'
        )

    def test_car_model(self):
        self.assertEqual(self.car.model, 'Model S')
        self.assertEqual(self.car.brand, 'Tesla')
        self.assertEqual(self.car.price, 79999.99)
        self.assertTrue(self.car.is_bought)
        self.assertEqual(self.car.buyer, self.user)
        self.assertEqual(str(self.car.buy_time), '2023-01-01 12:00:00+00:00')


# API Test Case
class CarAPITestCase(APITestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username='testuser', password='12345')
        cls.car = Car.objects.create(
            model='Model S',
            brand='Tesla',
            price='79999.99',
            is_bought=True,
            buyer=cls.user,
            buy_time='2023-01-01T12:00:00Z'
        )
        cls.list_url = reverse('car-list-create')
        cls.detail_url = reverse('car-detail', args=[cls.car.id])

    def test_get_car_list(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['model'], 'Model S')

    def test_create_car(self):
        data = {
            'model': 'Model 3',
            'brand': 'Tesla',
            'price': '35999.99',
            'is_bought': False,
        }
        response = self.client.post(self.list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['model'], 'Model 3')

    def test_get_car_detail(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['model'], 'Model S')

    def test_update_car(self):
        data = {
            'model': 'Model X',
            'brand': 'Tesla',
            'price': '89999.99',
            'is_bought': True,
            'buyer': self.user.id,
            'buy_time': '2023-01-02T12:00:00Z'
        }
        response = self.client.put(self.detail_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['model'], 'Model X')

    def test_delete_car(self):
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Car.objects.count(), 0)
