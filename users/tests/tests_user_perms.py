from rest_framework.test import APITestCase
from rest_framework import status

from sections.tests.utils import get_member_user


class UserTestCase(APITestCase):
    """
    Test for model Content
    work for both OVERALL and LOCAL launch
    (Тесты для модели контент
    работают как для ЛОКАЛЬНОГО так и ОБЩЕГО запуска
    """

    def setUp(self) -> None:
        """
        Basic setup
        (Базовые настройки)
        """
        self.user = get_member_user()
        response = self.client.post('/users/token/', {"email": "tester_member@test1.com", "password": "qwerty"})
        self.access_token = response.json().get("access")
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

    def test_user_delete(self):
        response = self.client.delete('/users/16/delete/')
        # print(response)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_users_list(self):
        response = self.client.get('/users/')
        # print(response.json())
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
