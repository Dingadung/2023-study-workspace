from my_api.models import TodoModel
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import TodoPostSerializer

from django.http.response import HttpResponse
from django.shortcuts import render
from rest_framework import status


class Todo(APIView):
    def get(self, request):
        all_todo = TodoModel.objects.all()
        serializer = TodoSerializer(all_todo, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def get_api(request):
    todo_posts = Post.objects.all()
    serailized_todo_posts= PostSerializer(todo_posts, many=True)
    return Response(serailized_posts.data)

@api_view(['POST'])
def post_api(request):
    if request.method == 'GET':
        return HttpResponse(status=200)
    if request.method == 'POST':
        serializer = PostSerializer(data = request.data, many=True)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data ,status=200)
        return Response(serializer.errors ,status=status.HTTP_400_BAD_REQUEST)