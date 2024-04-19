from django.db import models
from django.contrib.auth.models import User

class WeightInput(models.Model):
    age = models.IntegerField(default=0)
    gender = models.CharField(max_length=10, default='')
    activity_level = models.IntegerField(default=1)
    weight_kg = models.FloatField(default=0)
    height_cm = models.FloatField(default=0)
    target_weight = models.FloatField(default=0)
    current_weight = models.FloatField(default=0)
    goal = models.CharField(max_length=50,default='')
    strategy = models.TextField()
    


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.PositiveIntegerField(null=True, blank=True)
    gender = models.CharField(max_length=10, null=True, blank=True)
    fitness_goals = models.TextField(null=True, blank=True)
    medical_history = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.user.username