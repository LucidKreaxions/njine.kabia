from django.contrib import admin
from .models import RoomBooking, ActivityBooking

# Register your models here.
@admin.register(RoomBooking)
class RoomBookingAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "room", "check_in", "check_out", "created_at")
    list_filter = ("check_in", "check_out")


@admin.register(ActivityBooking)
class ActivityBookingAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "activity", "date", "participants", "created_at")
    list_filter = ("date",)
