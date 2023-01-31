from rest_framework import serializers
from .models import House2


class HouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = House2
        fields = "__all__"