from django.db import models

# Create your models here.
class Tasks(models.Model):
    name=models.CharField(max_length=64)
    def __str__(self):
        return f"{self.name}"