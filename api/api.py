from ninja import NinjaAPI
from .schema import GoalSchema, SolutionSchema, CategorySchema, NotFoundSchema
from .models import Goal, Category, Solution
import os

api = NinjaAPI()

@api.get("/goal/{goal_id}", response={200 : GoalSchema, 404 : NotFoundSchema})
def getGoals(request, goal_id: int ):
    try:
        goal = Goal.objects.get(pk=goal_id)
        return 200, goal
    except:
        return 404 , {"message": "goal not found"}


