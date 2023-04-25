from ninja import Schema, ModelSchema
from .models import Goal, Category, Solution, Task, Journal
import datetime


class CategorySchema(Schema):
    categoryName : str

class GoalSchema(Schema):
    user : str
    goal : str
    currentDate : datetime.date
    completionDate : datetime.date

class SolutionSchema(Schema):
    goal : str
    solution : str

class TaskSchema(ModelSchema):
    class Config:
        model = Task
        model_fields = '__all__'

class NotFoundSchema(Schema):
    message: str

class JournalSchema(ModelSchema):
    class Config:
        model = Journal
        model_fields = '__all__'
