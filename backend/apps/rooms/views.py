from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from django.db import transaction

from apps.rooms.models import Room
from .models import RoomBooking
from .serializers import RoomBookingSerializer

# Create your views here.
# List all rooms
class RoomListView(generics.ListAPIView): # availability search engine

    serializer_class = RoomSerializer

    def get_queryset(self):

        queryset = Room.objects.all()

        check_in = self.request.query_params.get("check_in")
        check_out = self.request.query_params.get("check_out")

        if check_in and check_out:

            booked_rooms = RoomBooking.objects.filter(
                check_in__lt=check_out,
                check_out__gt=check_in
            ).values_list("room_id", flat=True)

            queryset = queryset.exclude(id__in=booked_rooms)

        return queryset


# Get a single room
class RoomDetailView(generics.RetrieveAPIView):

    queryset = Room.objects.all()
    serializer_class = RoomSerializer

    def retrieve(self, request, *args, **kwargs):

        room = self.get_object()

        check_in = request.query_params.get("check_in")
        check_out = request.query_params.get("check_out")

        serializer = self.get_serializer(room)
        data = serializer.data

        if check_in and check_out:

            conflict = RoomBooking.objects.filter(
                room=room,
                check_in__lt=check_out,
                check_out__gt=check_in
            ).exists()

            data["available"] = not conflict

        return Response(data)

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
