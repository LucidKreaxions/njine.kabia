from django.urls import path
from .views import FoodListView


urlpatterns = [
    path("menu/", FoodListView.as_view()),
]
