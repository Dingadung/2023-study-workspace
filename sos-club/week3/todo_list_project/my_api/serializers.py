from rest_framework import serializers
from .models import TodoModel

class TodoPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoModel
        fields = ['title', 'description', 'is_starred', 'create_time']
    title = serializers.CharField(max_length=100)
    description = serializers.TextField()
    is_starred = serializers.BooleanField()
    create_time = serializers.DateTimeField(input_formats=["%Y-%m-%d"])
    