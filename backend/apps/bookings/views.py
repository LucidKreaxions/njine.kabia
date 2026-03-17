from django.shortcuts import render
from rest_framework import generics
from .models import RoomBooking
from .serializers import RoomBookingSerializer

# Create your views here.
class RoomBookingCreateView(generics.CreateAPIView):

    serializer_class = RoomBookingSerializer

    def create(self, request, *args, **kwargs):

        room_id = request.data.get("room")
        check_in = request.data.get("check_in")
        check_out = request.data.get("check_out")

        with transaction.atomic():

            # Lock the room row
            room = Room.objects.select_for_update().get(id=room_id)

            # Check overlapping bookings
            conflict = RoomBooking.objects.filter(
                room=room,
                check_in__lt=check_out,
                check_out__gt=check_in
            ).exists()

            if conflict:
                return Response(
                    {"error": "Room already booked for these dates"},
                    status=status.HTTP_400_BAD_REQUEST
                )

            booking = RoomBooking.objects.create(
                user=request.user,
                room=room,
                check_in=check_in,
                check_out=check_out
            )

        serializer = RoomBookingSerializer(booking)
        return Response(serializer.data)

