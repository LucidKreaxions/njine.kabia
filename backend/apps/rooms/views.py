from django.shortcuts import render
from rest_framework import generics
from .models import Room
from .serializers import RoomSerializer

# Create your views here.
# List all rooms
class RoomListView(generics.ListAPIView):

    queryset = Room.objects.all()
    serializer_class = RoomSerializer


# Get a single room
class RoomDetailView(generics.RetrieveAPIView):

    queryset = Room.objects.all()
    serializer_class = RoomSerializer
