from ninja import Schema, ModelSchema
from .models import Goal, Category, Solution
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
    
class NotFoundSchema(Schema):
    message: str