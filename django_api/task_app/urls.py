from django.urls import path
from .views import create_task
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('add/', csrf_exempt(create_task)),
]