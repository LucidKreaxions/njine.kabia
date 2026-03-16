from django.shortcuts import render
from rest_framework import generics
from .models import RoomBooking
from .serializers import RoomBookingSerializer

# Create your views here.
class RoomBookingCreateView(generics.CreateAPIView):

    queryset = RoomBooking.objects.all()
    serializer_class = RoomBookingSerializer
