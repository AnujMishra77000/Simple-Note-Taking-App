"""from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from Note_app.models import Notes

class Create_NoteApiTest_Case(APITestCase):

    def test_create_note(self):
        
        url = reverse('Creating-note')  
        data = {
            'title': 'Test Note',
            'body': 'This is a test Note.'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Notes.objects.count(), 1)
        self.assertEqual(Notes.objects.get().title, 'Test Note')


    def test_fetch_note_by_id(self):
       
        note = Notes.objects.create(title='Test Note', body='This is a test note.')
        url = reverse('Fetching-Note', args=[note.id])  
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Test Note')
   
    def test_query_notes_by_title_substring(self):
        
        Notes.objects.create(title='Important Note', body='This is an important note.')
        Notes.objects.create(title='Another Note', body='Just another note.')
        url = reverse('Search_by_Query')  
        response = self.client.get(url, {'search': 'title_name'})  
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Existing Note')
 
    def test_update_note(self):
        
        note = Notes.objects.create(title='Old Title', body='Old body text.')
        url = reverse('Updating-Note', args=[note.id])  
        data = {
            'title': 'Updated Title',
            'body': 'Updated body text.'
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        note.refresh_from_db()
        self.assertEqual(note.title, 'Updated Title')
        self.assertEqual(note.body, 'Updated body text.')"""

