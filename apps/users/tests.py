from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from apps.users.models import User, TypeUser


class UserTests(APITestCase):

    def setUp(self):
        TypeUser.objects.get_or_create(id=1, name='driver')
        TypeUser.objects.get_or_create(id=2, name='passenger')
        TypeUser.objects.get_or_create(id=3, name='manager')

    def test_register_account(self):
        url = reverse('sign-in')
        data = {'phone_number': '77059943864', 'test': True}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().phone, '77059943864')

    def test_register_account_not_valid(self):
        url = reverse('sign-in')
        data = {'phone_number': '770599438646ңң', 'test': True}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
