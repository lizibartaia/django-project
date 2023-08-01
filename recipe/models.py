from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Recipe(models.Model):
    name = models.CharField(max_length=100)
    ingredient = models.CharField(max_length=100)
    time = models.FloatField()
    process = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.name