from rest_framework import serializers
from .models import Activity


# converts Activity objects into JSON responses
class ActivitySerializer(serializers.ModelSerializer):

    class Meta:
        model = Activity
        fields = "__all__"
