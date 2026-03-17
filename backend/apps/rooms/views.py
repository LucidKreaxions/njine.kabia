from rest_framework import generics
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from datetime import date
from .models import Room
from .serializers import RoomSerializer
from apps.bookings.models import RoomBooking
from apps.bookings.serializers import RoomBookingSerializer

# Create your views here.
# List all rooms
class RoomListView(generics.ListAPIView): # availability search engine

    serializer_class = RoomSerializer

    def get_queryset(self):

        queryset = Room.objects.all()

        check_in = self.request.query_params.get("check_in")
        check_out = self.request.query_params.get("check_out")

        # ✅ PRO LEVEL VALIDATION
        if check_in and check_out:

            check_in = date.fromisoformat(check_in)
            check_out = date.fromisoformat(check_out)

            if check_in >= check_out:
                raise ValidationError("check_out must be after check_in")

            if check_in < date.today():
                raise ValidationError("Cannot book past dates")

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

            check_in = date.fromisoformat(check_in)
            check_out = date.fromisoformat(check_out)

            # ✅ PRO VALIDATION
            if check_in >= check_out:
                raise ValidationError("check_out must be after check_in")

            if check_in < date.today():
                raise ValidationError("Cannot book past dates")

            conflict = RoomBooking.objects.filter(
                room=room,
                check_in__lt=check_out,
                check_out__gt=check_in
            ).exists()

            data["available"] = not conflict

        return Response(data)
