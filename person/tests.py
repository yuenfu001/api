from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from .models import Person

class PersonAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.person_data = {
            "first_name": "John",
            "middle_name": "Doe",
            "last_name": "Smith",
            "gender": "male",
            "address": "123 Main Street"
        }

    def test_create_person(self):
        response = self.client.post('/api/persons/', self.person_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_read_person(self):
        person = Person.objects.create(**self.person_data)
        response = self.client.get(f'/api/persons/{person.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['first_name'], 'John')

    def test_update_person(self):
        person = Person.objects.create(**self.person_data)
        updated_data = {
            "first_name": "Updated",
            "middle_name": "Name",
            "last_name": "Here",
            "gender": "female",
            "address": "456 Elm Street"
        }
        response = self.client.put(f'/api/persons/{person.id}/', updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['first_name'], 'Updated')

    def test_delete_person(self):
        person = Person.objects.create(**self.person_data)
        response = self.client.delete(f'/api/persons/{person.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
