from .models import House
# from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import HouseSerializer

from django.http.response import HttpResponse
from django.shortcuts import render
from rest_framework import status
from django.http import Http404

from django.shortcuts import get_object_or_404


# class Houses(APIView):
#     def get(self, request):
#         all_houses = House.objects.all()
#         serializer = HouseSerializer(all_houses, many=True)
#         return Response(serializer.data)

def getPk(md, pk):
    primaryKey = md.objects.get(pk = pk)
    return primaryKey
    
@api_view(["GET", "POST"])
def houses(request):
    if request.method == "GET":
        all_houses = House.objects.all()
        serializer = HouseSerializer(all_houses, many=True)
        return Response(serializer.data)
    else:
        serializer = HouseSerializer(data=request.data)
        if serializer.is_valid():
            new_house = serializer.save()
            serializer = HouseSerializer(new_house)
            return Response(serializer.data ,status=status.HTTP_201_CREATED)
        return Response(serializer.errors ,status=status.HTTP_400_BAD_REQUEST)

@api_view()
def house(request, pk):
    try:
        house = getPk(House, pk)
    except House.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = HouseSerializer(house)
    return Response(serializer.data)
