from ninja import NinjaAPI
from ninja.responses import codes_2xx
from django.shortcuts import get_object_or_404
import asyncio
from asgiref.sync import sync_to_async
from .schema import GoalSchema, SolutionSchema, CategorySchema, NotFoundSchema
from .models import Goal, Category, Solution
import os
from datetime import datetime
from .meilleur import createSolution

api = NinjaAPI()

@api.get("/goal/{goal_id}", response={200 : GoalSchema, 404 : NotFoundSchema})
async def getGoals(request, goal_id: int ):
    try:
        goal = Goal.objects.get(pk=goal_id)
        return 200, goal
    except:
        return 404 , {"message": "goal not found"}


@api.post("goals/", response={201: GoalSchema})
def createGoal(request, goal: GoalSchema):
    goal = (Goal.objects.create(**goal.dict()))
    return 201, goal


@api.api_operation(["POST","GET"] , "solution/{goal_id}", response={codes_2xx: SolutionSchema, 404: NotFoundSchema})
async def getSolution(request, goal_id: int):
    gol = Goal.objects.filter(pk=goal_id)
    goal_obj = await sync_to_async(get_object_or_404)(Goal, pk=goal_id)
    # currentDate = datetime.strptime(goal.currentDate , '%m-%d-%Y').date()
    # # startDate =  currentDate
    # # completionDate = datetime.strptime(goal.completionDate , '%m-%d-%Y').date()
    # endDate = datetime.date(completionDate)


    solution = await (createSolution(goal_obj.goal))
    advice = await sync_to_async(Solution.objects.create)(goal=goal_obj, solution=solution)
    

    return 201, advice

