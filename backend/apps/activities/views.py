from django.shortcuts import render
from rest_framework import generics
from .models import Activity
from .serializers import ActivitySerializer

# Create your views here.
# List all activities
class ActivityListView(generics.ListAPIView):

    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer


# Get one activity
class ActivityDetailView(generics.RetrieveAPIView):

    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
