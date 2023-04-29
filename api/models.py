from django.db import models
from django.conf import settings
from markdownfield.models import MarkdownField, RenderedMarkdownField
from markdownfield.validators import VALIDATOR_STANDARD
# Create your models here
# 


class Goal(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    goal = models.TextField()
    currentDate = models.DateField(auto_now=True)
    completionDate = models.DateField()

    
class Solution(models.Model):
    goal = models.OneToOneField(Goal, on_delete=models.CASCADE)
    solution = models.TextField()


class Task(models.Model):
    solution = models.ForeignKey(Solution, on_delete=models.CASCADE)
    task = models.TextField()
    nextUp = 0
    inProgress = 1
    complete = 2
    archive = 3

    statuses = (('next up', nextUp), ('In Progress', inProgress), ('Complete', complete), ('Archive', archive))
    status = models.PositiveSmallIntegerField(choices = statuses , blank = True , null=True)
    date_created = models.DateTimeField(auto_created=True)

    def __str__(self):
        return f"{solution.id} task"
    

class Journal(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = MarkdownField(rendered_field='text_rendered', validator=VALIDATOR_STANDARD)
    text_rendered = RenderedMarkdownField()
    date = models.DateTimeField(auto_now=True)


class Category(models.Model):
    categoryName = models.CharField(max_length=255)
    goalsInCategory = models.ManyToManyField(Goal)
    tasksInCategory = models.ManyToManyField(Task)
  


    def __str__(self):
        return self.categoryName




