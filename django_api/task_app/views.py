import json

from django.http import HttpResponse, JsonResponse

from .models import Tasks

# Create your views here.
def create_task(request):
    raw_data = request.body
    conv_data = json.loads(request.body)
    # save to db
    data = Tasks(**conv_data)
    data.save()

    return JsonResponse({"data": "data created succesfully"}, status=201)


   


