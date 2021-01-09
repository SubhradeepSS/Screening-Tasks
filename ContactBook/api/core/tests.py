from django.test import TestCase, Client
from .models import Contact
from rest_framework import status
from .serializers import ContactSerializer
import json

# Create your tests here.
client = Client()
BASE_URL = 'http://127.0.0.1:8000/api/'

class ContactTest(TestCase):
    def setUp(self):
        self.test1 = Contact.objects.create(email='test1@test.com', name='test1')
        self.test2 = Contact.objects.create(email='test2@test.com', name='test2')
        self.test3 = Contact.objects.create(email='test3@test.com', name='test3')


    def test_ContactsView_GET(self):
        response = client.get(BASE_URL)
        contacts = Contact.objects.all()
        serialized_contacts = ContactSerializer(instance=contacts, many=True)
        self.assertEqual(serialized_contacts.data, response.data['results'])
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_ContactsView_POST_valid(self):
        valid_payload = {
            'name': 'Muffin',
            'email': 'muffin@test.com'
        }
        valid_response = client.post(BASE_URL, data=json.dumps(valid_payload), content_type='application/json')
        self.assertEqual(valid_response.status_code, status.HTTP_201_CREATED)


    def test_ContactsView_POST_invalid(self):
        invalid_payload = {
            'name': '',
            'email': ''
        }
        invalid_response = client.post(BASE_URL, data=json.dumps(invalid_payload), content_type='application/json')
        self.assertEqual(invalid_response.status_code, status.HTTP_400_BAD_REQUEST)

    
    def test_ContactView_GET_valid(self):
        valid_response = client.get(BASE_URL + str(self.test1.pk))
        test1 = Contact.objects.get(pk=self.test1.pk)
        self.assertEqual(valid_response.data, ContactSerializer(test1).data)
        self.assertEqual(valid_response.status_code, status.HTTP_200_OK)

    def test_ContactsView_GET_invalid(self):
        invalid_response = client.get(BASE_URL + '100')
        self.assertEqual(invalid_response.status_code, status.HTTP_404_NOT_FOUND)


    def test_ContactView_DELETE_valid(self):
        valid_response = client.delete(BASE_URL + str(self.test1.pk))
        self.assertEqual(valid_response.status_code, status.HTTP_204_NO_CONTENT)

    def test_ContactView_DELETE_invalid(self):
        invalid_response = client.delete(BASE_URL + '100')
        self.assertEqual(invalid_response.status_code, status.HTTP_404_NOT_FOUND)


    def test_ContactView_PUT_valid(self):
        valid_payload = {
            'name': 'test1',
            'email': 'test1@user.com'
        }
        valid_response = client.put(BASE_URL + str(self.test1.pk), data=valid_payload, content_type='application/json')
        self.assertEqual(valid_response.status_code, status.HTTP_200_OK)

    def test_ContactView_PUT_invalid(self):
        invalid_payload = {
            'name': '',
            'email': ''
        }
        invalid_response = client.put(BASE_URL + str(self.test1.pk), data=invalid_payload, content_type='application/json')
        self.assertEqual(invalid_response.status_code, status.HTTP_400_BAD_REQUEST)
    

    def test_SearchNameView_present(self):
        name_part = 't2'
        response = client.get(BASE_URL + 'search/name/' + name_part)
        self.assertIn(ContactSerializer(self.test2).data, response.data['results'])
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_SearchNameView_absent(self):
        name_part = 'dfvb'
        response = client.get(BASE_URL + 'search/name/' + name_part)
        self.assertNotIn(ContactSerializer(self.test2).data, response.data['results'])
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    
    def test_SearchEmailView_present(self):
        email = 'test2@test.com'
        response = client.get(BASE_URL + 'search/email/' + email)
        self.assertIn(ContactSerializer(self.test2).data, response.data['results'])
        self.assertEqual(1, len(response.data['results']))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_SearchEmailView_absent(self):
        email = 'dfvb@fv.com'
        response = client.get(BASE_URL + 'search/email/' + email)
        self.assertEqual(0, len(response.data['results']))
        self.assertEqual(response.status_code, status.HTTP_200_OK)