from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .models import Person
from .serializers import Personserializer
# Create your views here.


@api_view(["GET","POST"])
def person(request):
    if request.method =="GET":
        people = Person.objects.all()
        serialize = Personserializer(people, many=True)
        content = {
            "person":serialize.data
        }
        return Response(content)
    if request.method =="POST":
        create = Personserializer(data=request.data)
        if create.is_valid():
            create.save()
            return Response(create.data, status = status.HTTP_201_CREATED)

@api_view(["GET","PUT","DELETE"])
def update_person(request,pk):
    try:
        people = Person.objects.all()
        unique = people.get(id=pk)
    except Person.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND) 

    if request.method == "GET":
        check = Personserializer(unique)
        return Response(check.data)
    elif request.method == "PUT":
        update = Personserializer(unique, data=request.data)
        if update.is_valid():
            update.save()
            return Response(update.data)
        return Response(update.error, status = status.HTTP_404_BAD_REQUEST)
    elif request.method == "DELETE":
        unique.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)