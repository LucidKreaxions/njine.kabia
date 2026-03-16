from rest_framework import serializers
from .models import RoomBooking


class RoomBookingSerializer(serializers.ModelSerializer):

    class Meta:
        model = RoomBooking
        fields = "__all__"

    def validate(self, data):

        room = data["room"]
        check_in = data["check_in"]
        check_out = data["check_out"]

        conflicting_bookings = RoomBooking.objects.filter(
            room=room,
            check_in__lt=check_out,
            check_out__gt=check_in
        )

        if conflicting_bookings.exists():
            raise serializers.ValidationError(
                "This room is already booked for the selected dates."
            )

        return data
