from django.urls import path
from .views import RoomBookingCreateView


urlpatterns = [

    path("", RoomBookingCreateView.as_view(), name="room-booking"),

]
