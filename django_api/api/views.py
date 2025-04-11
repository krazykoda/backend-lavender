import json
from django.shortcuts import render
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.http import HttpResponse, JsonResponse

from rest_framework.response import Response

from .models import Test
from .serializers import TestSerializer

import random
import string



# Create your views here.
data = []
task = []

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def index(request):
    return JsonResponse({"message": "Hello World"})


@permission_classes([IsAuthenticated])
def add(request):
    raw_data = request.body
    conv_data = json.loads(request.body)
    task.append(conv_data)

    length = 8
    random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=length))

    data.append(random_string)
    return JsonResponse({"data": task}, status=201)


def create_task(request):
    print(request.POST)


def list(request):
    return JsonResponse({"data": data})


@api_view(['POST'])
def create_test(request):

    serializer = TestSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save(tested=False)

    return Response(data=serializer.data, status=201)



@api_view(['GET'])
def list_test(request):

    tests = Test.objects.all()
    serializer = TestSerializer(tests, many=True)
    return Response(data=serializer.data, status=200)




# django-admin startproject weather-api

