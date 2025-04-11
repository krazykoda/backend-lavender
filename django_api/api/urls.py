from django.urls import path
from .views import index, add, list, create_test, list_test
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('', index),
    path('add/', csrf_exempt(add)),
    path('list/', list),
    path('create-test/', create_test),
    path('list-test/', list_test),
]