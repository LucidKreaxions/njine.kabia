from django.urls import path
from .views import RoomListView, RoomDetailView


urlpatterns = [

    # List all rooms + availability search
    path("", RoomListView.as_view(), name="room-list"),

    # Get single room (with optional availability check)
    path("<int:pk>/", RoomDetailView.as_view(), name="room-detail"),

]
