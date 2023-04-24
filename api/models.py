from django.db import models
from django.conf import settings
# Create your models here
# 


class Goal(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    goal = models.TextField()
    currentDate = models.DateField(auto_now=True)
    completionDate = models.DateField()

    

class Category(models.Model):
    categoryName = models.TextField()
    goalsInCategory = models.ManyToManyField(Goal)

    def __str__(self):
        return self.categoryName
    


class Solution(models.Model):
    goal = models.OneToOneField(Goal, on_delete=models.CASCADE)
    solution = models.TextField()