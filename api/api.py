from ninja import NinjaAPI
from ninja.responses import codes_2xx
from django.shortcuts import get_object_or_404
import asyncio
from asgiref.sync import sync_to_async , async_to_sync
from .schema import GoalSchema, SolutionSchema, CategorySchema, NotFoundSchema, TaskSchema, JournalSchema
from .models import Goal, Category, Solution, Task, Journal
import os
from datetime import datetime
from .meilleur import createSolution, createTasks, categorize
from channels.db import database_sync_to_async

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


@api.delete("goal/{goal_id}", response={200: None, 404: NotFoundSchema})
def deleteGoal(request, goal_id: int):
    try:
        goal = Goal.objects.get(pk=goal_id)
        goal.delete()
        return goal
    except Goal.DoesNotExist as e:
        return 404, {"message" : "Could not find goal"}





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


@api.post("tasks/", response={201: TaskSchema})
def createTask(request, task: TaskSchema):
    task = Task.objects.create(**task.dict())
    return 201, task

@api.get("task/{task_id}", response={201: TaskSchema, 404: NotFoundSchema})
def getTask(request, task_id: int):
    try:
        task = Task.objects.get(pk=task_id)
        return 200, task
    except:
        return 404 , {"message": "goal not found"}


@api.put("task/{task_id}", response={200: TaskSchema, 404: NotFoundSchema})
def changeTask(request, task_id: int, data: TaskSchema):
    try:
        task = Task.object.get(pk=task_id)
        for attribute, value in data.dict().items():
            setattr(task, attribute, value)
        task.save()
        return 200, task
    except Task.DoesNotExist as e:
        return 404 , {"message": "Could not find track"}

@api.delete("task/{task_id}", response={200: None, 404: NotFoundSchema})
def deleteTask(request, task_id: int):
    try:
        task = Task.objects.get(pk=task_id)
        task.delete()
        return task
    except Task.DoesNotExist as e:
        return 404, {"message" : "Could not find track"}


@api.post("journal/", response={201: JournalSchema})
def createJournal(request, journal: JournalSchema):
    journal = journal.objects.create(**journal.dict())
    journal.save()
    return 201, journal

@api.get("journal/{journal_id}", response={200: JournalSchema, 404: NotFoundSchema})
def getJournal(request, journal_id: int):
    try:
        journal = Journal.objects.get(pk=journal_id)
        return 200, journal
    except:
        return 404, {"message": "Journal entry not found"}

@api.put("journal/{journal_id}", response={200: JournalSchema, 404: NotFoundSchema})
def alterJournal(request, journal_id: int):
    try:
        journal = Journal.object.get(pk=journal_id)
        for attribute, value in data.dict().items():
            setattr(journal, attribute, value)
        journal.save()
        return 200, journal
    except Journal.DoesNotExist as e:
        return 404 , {"message": "Could not find journal"}

@api.delete("journal/{journal_id}", response={200: None, 404: NotFoundSchema})
def deleteCategory(request, journal_id: int):
    try:
        journal = Journal.objects.filter(pk=journal_id)
        journal.delete()
        return 200, None
    except:
        return 404 , {"message": "Journal not found"}


@database_sync_to_async
def get_goal_objects():
    return list(Goal.objects.all())

@database_sync_to_async
def get_task_objects():
    return list(Task.objects.all())

@api.post("category/", response={201: CategorySchema})
def makeCategories(request, category: CategorySchema):
    
    category = Category.objects.create(**category.dict())
    category.save()
    return 201, category

@api.get("category/{category_id}", response={200: CategorySchema, 404: NotFoundSchema})
def getCategory(request, category_id: int):
    try:
        category = Category.objects.filter(pk=category_id)
        return 200, category
    except: 
        return 404, {"message": "Category not found"}

@api.put("category/{category_id}", response={200: CategorySchema, 404: NotFoundSchema})
def alterCategory(request, category_id: int):
    try:
        category = Category.object.get(pk=category_id)
        for attribute, value in data.dict().items():
            setattr(category, attribute, value)
        category.save()
        return 200, category
    except Category.DoesNotExist as e:
        return 404 , {"message": "Could not find track"}

@api.delete("category/{category_id}", response={200: None, 404: NotFoundSchema})
def deleteCategory(request, category_id: int):
    try:
        category = Category.objects.filter(pk=category_id)
        category.delete()
        return 200, None
    except:
        return 404 , {"message": "Category not found"}


