from django.db import models

# Create your models here.


class Test(models.Model):
    name = models.CharField(max_length=50, blank=True)
    tested = models.BooleanField(default=True)


    def __str__(self):
        return f"{self.name} ---> {self.tested}"
