from django.db import models

# Create your models here
# 

class Category(models.Model):
    categoryName = models.TextField()
    

class Goal(models.Model):
    goal = models.TextField()
    currentDate = models.DateField(auto_now=True)
    completionDate = models.DateField()
    goalCategory  = models.OneToOneField(Category, on_delete=models.CASCADE)


class Solution(models.Model):
    goal = models.OneToOneField(Goal, on_delete=models.CASCADE)
    solution = models.TextField()