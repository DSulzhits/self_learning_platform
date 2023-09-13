from rest_framework.test import APITestCase
from rest_framework import status

from sections.models import Section
from sections.tests.utils import get_admin_user


class SectionTestCase(APITestCase):
    """
    Tests for model Section, 2 options:
    1) OVERALL test that can be run from the terminal
    2) LOCAL test for this file only
    (Тесты для модели Section, 2 опции:
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
        self.test_section = Section.objects.create(
            title='test_section',
            description='test_description'
        )

    """
    if you want to run OVERALL test from terminal
    (если вы хотите запустить ОБЩИЙ тест из терминала)
    """


    def test_section_create(self):
        data = {
            'title': 'test_section_create',
            'description': 'test_section_description_create'
        }
        response = self.client.post('/section/create/', data=data)
        # print(response.json())
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json()['title'], 'test_section_create')

    def test_section_delete(self):
        response = self.client.delete('/section/8/delete/')
        # print(response)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_section_detail(self):
        response = self.client.get('/section/9/')
        # print(response.json())
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['title'], 'test_section')
        self.assertEqual(response.json()['description'], 'test_description')

    def test_section_list(self):
        response = self.client.get('/section/')
        # print(response.json())
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['results'][0]['title'], 'test_section')

    def test_section_update(self):
        data = {
            'title': 'test_section_put',
            'description': 'test_section_description_put'
        }
        response = self.client.put('/section/11/update/', data=data)
        # print(response.json())
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['title'], 'test_section_put')
        self.assertEqual(response.json()['description'], 'test_section_description_put')

    # """
    # if you want to run LOCAL test only for the current file
    # (если вы хотите запустить ЛОКАЛЬНЫЙ тест только для этого файла)
    # """
    #
    # def test_section_create(self):
    #     data = {
    #         'title': 'test_section_create',
    #         'description': 'test_section_description_create'
    #     }
    #     response = self.client.post('/section/create/', data=data)
    #     # print(response.json())
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    #     self.assertEqual(response.json()['title'], 'test_section_create')
    #
    # def test_section_delete(self):
    #     response = self.client.delete('/section/3/delete/')
    #     # print(response)
    #     self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    #
    # def test_section_detail(self):
    #     """if you want start test only in this file"""
    #     response = self.client.get('/section/4/')
    #     # print(response.json())
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertEqual(response.json()['title'], 'test_section')
    #     self.assertEqual(response.json()['description'], 'test_description')
    #
    # def test_section_list(self):
    #     response = self.client.get('/section/')
    #     # print(response.json())
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertEqual(response.json()['results'][0]['title'], 'test_section')
    #
    # def test_section_update(self):
    #     data = {
    #         'title': 'test_section_put',
    #         'description': 'test_section_description_put'
    #     }
    #     response = self.client.put('/section/6/update/', data=data)
    #     # print(response.json())
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertEqual(response.json()['title'], 'test_section_put')
    #     self.assertEqual(response.json()['description'], 'test_section_description_put')
