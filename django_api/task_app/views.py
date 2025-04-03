import json

from django.core import serializers
from django.http import HttpResponse, JsonResponse

from .models import Tasks

# Create your views here.
def create_task(request):
    if request.method == "POST":
        # request.body is a json
        raw_data = request.body
       

        # convert json into dictionary
        conv_data = json.loads(raw_data)

        print(conv_data)
        

        name = conv_data.get("name")
        description = conv_data.get("description")

        # check if request body has name
        if not name:
            return JsonResponse({"error": "Please provide the name"}, status=400)


        # save to db
        # data = Tasks(name=name, description=description)
        # data.save()
        data = Tasks.objects.create(**conv_data)   

        json_data = serializers.serialize('json', data) 

        return JsonResponse({"data": "data created succesfully"}, status=201)

    else:
        return JsonResponse({"error": "Method not allowed"}, status=405)



# List Tasks
def list_tasks(request):
    if request.method == "GET":
        data = Tasks.objects.all()

        # serialize query response
        json_data = serializers.serialize('json', data) 
        json_data = json.loads(json_data)

        return JsonResponse({"data": json_data}, status=200)

    else:
        return JsonResponse({"error": "Method not allowed"}, status=405)



# Get One Task
def get_task(request, task_id):
    print(task_id)
    data = Tasks.objects.filter(pk=task_id).first()
    
    # You can only serialize a list
    json_data = serializers.serialize('json', [data]) 
    json_data = json.loads(json_data)

    return JsonResponse({"data": json_data}, status=200)



# Update a task
def update_task(request, task_id):
    raw_data = request.body
    dict_data = json.loads(raw_data)

    # csome validations 

    # Update task
    Tasks.objects.filter(pk=task_id).update(**dict_data)

    return JsonResponse({"message": "task updated"}, status=200)





# Delete a task



   


