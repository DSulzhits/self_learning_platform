from rest_framework.test import APITestCase
from rest_framework import status

from sections.models import Section
from sections.tests.utils import get_user


class SectionTestCase(APITestCase):
    """Test for model Section"""

    def setUp(self) -> None:
        """Basic setup"""
        self.user = get_user()
        response = self.client.post('/users/token/', {"email": "tester@test1.com", "password": "qwerty"})
        self.access_token = response.json().get("access")
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        self.test_section = Section.objects.create(
            title='test_section',
            description='test_description'
        )

    def test_section_create(self):
        data = {
            'title': 'test_section_create',
            'description': 'test_section_description_create'
        }
        response = self.client.post('/section/create/', data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json()['title'], 'test_section_create')

    def test_section_delete(self):
        response = self.client.delete('/section/3/delete/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_section_detail(self):
        response = self.client.get('/section/4/')
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
        response = self.client.put('/section/6/update/', data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['title'], 'test_section_put')
        self.assertEqual(response.json()['description'], 'test_section_description_put')
