from django.urls import path
from .views import index, add, list
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('', index),
    path('add/', csrf_exempt(add)),
    path('list/', list),
]