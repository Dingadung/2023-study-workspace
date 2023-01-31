from .models import House2
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import HouseSerializer

from django.http.response import HttpResponse
from django.shortcuts import render
from rest_framework import status
from django.http import Http404

from django.shortcuts import get_object_or_404



class Houses(APIView):
    def get(self, request):
        all_houses = House2.objects.all()
        serializer = HouseSerializer(all_houses, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = HouseSerializer(data=request.data)
        if serializer.is_valid():
            new_house = serializer.save()
            serializer = HouseSerializer(new_house)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors ,status=status.HTTP_400_BAD_REQUEST)

class HouseDetail(APIView):
    def get(self, request, pk):
        try: 
            house = House2.objects.get(pk=pk)
        except House2.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = HouseSerializer(house)
        return Response(serializer.data)

    def put(self, request, pk):
        house = House2.objects.get(pk=pk)
        serializer = HouseSerializer(house, data=request.data, partial=True)
        if serializer.is_valid():
            updated_house = serializer.save()
            serializer = HouseSerializer(updated_house)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors ,status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        house = House2.objects.get(pk=pk)
        house.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)