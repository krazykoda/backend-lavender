from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator 

# Create your models here.
# created_at
# name 
# description 
# completed

class Tasks(models.Model):
    name = models.CharField(max_length=255, null=False)
    description = models.TextField(null=True, blank=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    progress = models.PositiveSmallIntegerField(default=1,  validators=[MinValueValidator(1), MaxValueValidator(100)])


    def __str__(self):
        return f"{self.name}=>{self.completed}"


