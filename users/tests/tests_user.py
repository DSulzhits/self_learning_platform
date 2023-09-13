from rest_framework.test import APITestCase
from rest_framework import status

from sections.tests.utils import get_admin_user


class UserTestCase(APITestCase):
    """
    Tests for model User, 2 options:
    1) OVERALL test that can be run from the terminal
    2) LOCAL test for this file only
    (Тесты для модели User, 2 опции:
    1) ОБЩИЙ для запуска тестов из терминала
    2) ЛОКАЛЬНЫЙ для запуска тестов только в этом файле)
    """

    def setUp(self) -> None:
        """
        Basic setup
        (Базовые настройки)
        """
        self.user = get_admin_user()
        response = self.client.post('/users/token/', {"email": "tester@test1.com", "password": "qwerty"})
        self.access_token = response.json().get("access")
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

    """
    if you want to run OVERALL test from terminal
    (если вы хотите запустить ОБЩИЙ тест из терминала)
    """

    def test_user_create(self):
        data = {
            'email': 'tester_create@test.com',
            'role': 'member',
            'password': '123321'
        }
        response = self.client.post('/users/create/', data=data)
        # print(response.json())
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json()['email'], 'tester_create@test.com')

    def test_user_delete(self):
        response = self.client.delete('/users/13/delete/')
        # print(response)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_user_detail(self):
        response = self.client.get('/users/14/')
        # print(response.json())
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['email'], 'tester@test1.com')
        self.assertEqual(response.json()['role'], 'moderator')
        self.assertEqual(self.user.__str__(), 'tester@test1.com')

    def test_users_list(self):
        response = self.client.get('/users/')
        # print(response.json())
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()[0]['email'], 'tester@test1.com')

    def test_user_update(self):
        data = {
            'email': 'tester_updated@test1.com',
        }
        response = self.client.patch('/users/15/update/', data=data)
        # print(response.json())
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # """
    # if you want to run LOCAL test only for the current file
    # (если вы хотите запустить ЛОКАЛЬНЫЙ тест только для этого файла)
    # """
    #
    # def test_user_create(self):
    #     data = {
    #         'email': 'tester_create@test.com',
    #         'role': 'member',
    #         'password': '123321'
    #     }
    #     response = self.client.post('/users/create/', data=data)
    #     # print(response.json())
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    #     self.assertEqual(response.json()['email'], 'tester_create@test.com')
    #
    # def test_user_delete(self):
    #     response = self.client.delete('/users/3/delete/')
    #     # print(response)
    #     self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    #
    # def test_user_detail(self):
    #     response = self.client.get('/users/4/')
    #     # print(response.json())
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertEqual(response.json()['email'], 'tester@test1.com')
    #     self.assertEqual(response.json()['role'], 'moderator')
    #
    # def test_users_list(self):
    #     response = self.client.get('/users/')
    #     # print(response.json())
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertEqual(response.json()[0]['email'], 'tester@test1.com')
    #
    # def test_user_update(self):
    #     data = {
    #         'email': 'tester_updated@test1.com',
    #     }
    #     response = self.client.patch('/users/5/update/', data=data)
    #     # print(response.json())
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
