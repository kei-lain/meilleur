from ninja import NinjaAPI
from ninja.responses import codes_2xx
from django.shortcuts import get_object_or_404
import asyncio
from asgiref.sync import sync_to_async
from .schema import GoalSchema, SolutionSchema, CategorySchema, NotFoundSchema, TaskSchema
from .models import Goal, Category, Solution, Task, Journal
import os
from datetime import datetime
from .meilleur import createSolution, createTasks

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
    solution = await (createSolution(goal_obj.goal))
    advice = await sync_to_async(Solution.objects.create)(goal=goal_obj, solution=solution)
    

    return 201, advice


@api.api_operation(["POST","GET"], "ai-task/{solution_id}", response={codes_2xx: TaskSchema})
async def getAITasks(request, solution_id: int):
    solution = Solution.objects.filter(pk=solution_id)
    solution_obj = await sync_to_async(get_object_or_404)(Solution , pk=solution_id)
    # goal = sync_to_async(solution_obj.goal)
    futures = asyncio.ensure_future(createTasks(solution_obj.solution))
    currentTime = datetime.now()

    
    for future in asyncio.as_completed([futures]):
        tasks = await future
        for task in tasks:
            print(task)
            new_task = await sync_to_async(Task.objects.create)(solution=solution_obj,task=task, status=0, date_created=currentTime)
        return 201, new_task



