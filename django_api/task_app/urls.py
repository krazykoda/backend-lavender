from django.urls import path
from .views import create_task, list_tasks, get_task, update_task
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('add/', csrf_exempt(create_task)),
    path("list/", list_tasks, name="list_tasks"),
    path("get/<int:task_id>/", get_task),
    path("update/<int:task_id>/", csrf_exempt(update_task))
]