from distutils.log import debug
from urllib import response
from django.http import JsonResponse
from .models import Drink
from .serializers import DrinkSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
@api_view(['Get', 'Post'])
def drink_list(request, format=None):
    if request.method =='GET':
        drinks = Drink.objects.all()
        serealizer = DrinkSerializer(drinks, many=True)
        return Response(serealizer.data)
    if request.method == 'POST':
        serealizer = DrinkSerializer(data=request.data)
        if serealizer.is_valid():
            serealizer.save()
            return Response(serealizer.data, status=status.HTTP_201_CREATED)
@api_view(['GET', 'PUT', 'DELETE'])
def drink_detail(request, id, format=None):
    try:
        drink = Drink.objects.get(pk=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serializer = DrinkSerializer(drink)
        return Response(serializer.data)
    if request.method == "PUT":
        serializer = DrinkSerializer(drink, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
    if request.method == "DELETE":
        drink.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

