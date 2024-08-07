from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class UserScore(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_points = models.IntegerField(default=0)
    dateTime = models.DateTimeField(default=timezone.now)

    # def __str__(self):
    #     return f"{self.user.username}: {self.total_points} points on {self.dateTime}"

