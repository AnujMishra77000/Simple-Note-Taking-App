from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from Note_app.Api import serializers
from Note_app import models

class CreateNoteViewTestCase(APITestCase):
    
    def setUp(self):
        self.title = models.Notes.objects.create(title="note one", body="it first note")
        

    def test_createnote(self):
        data = {
            "title":"hello",
            "body":"hello i am test file"
        }
        response = self.client.post(reverse('Creating-Note'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_NoteById(self):
        response = self.client.get(reverse('Fetching_Note', args=(self.title.id,)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(models.Notes.objects.count(), 1)
        self.assertEqual(models.Notes.objects.get().title,"note one")
    
    def test_NoteByTitle(self):
        search_term='Test'
        response= self.client.get(reverse('Search_by_Query'),{'search':search_term})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_UpdateNote(self):
        data = {
            "title":"hello",
            "body":"hello i am Updated test file"
        }
        response = self.client.put(reverse('Updating-Note', args=(self.title.id,)), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)