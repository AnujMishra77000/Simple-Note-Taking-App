from rest_framework import generics, status
from rest_framework.response import Response
from Note_app.models import Notes
from Note_app.Api.serializers import NoteSerializer
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.exceptions import NotFound


class CreateNoteView(generics.CreateAPIView):
    queryset = Notes.objects.all()
    serializer_class = NoteSerializer

class FetchNotesbyIDView(APIView):
    def get(self, request, pk):
        try:
            data = Notes.objects.get(pk=pk)
        except Notes.DoesNotExist:
            return Response({'error': 'Not found Please enter Valid Note ID'}, status=status.HTTP_404_NOT_FOUND)

        serializer = NoteSerializer(data)
        return Response(serializer.data , status=status.HTTP_200_OK)

class SearchQueryNotesView(generics.ListAPIView):
    queryset = Notes.objects.all()
    serializer_class = NoteSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']
                
           
class UpdateNoteView(generics.UpdateAPIView):
    queryset = Notes.objects.all()
    serializer_class = NoteSerializer
    