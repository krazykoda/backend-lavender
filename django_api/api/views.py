import json
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

import random
import string



# Create your views here.
data = []
task = []

def index(request):
    return JsonResponse({"message": "Hello World"})


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





# django-admin startproject weather-api

