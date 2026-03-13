from django.shortcuts import render
from rest_framework import generics
from .models import FoodItem
from .serializers import FoodItemSerializer

# Create your views here.
class FoodListView(generics.ListAPIView):

    queryset = FoodItem.objects.all()

    serializer_class = FoodItemSerializer
