import openai
import asyncio
import os
from dotenv import load_dotenv
import asyncio


load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

# class Guide:
#     def __init__(self,solution, further, backward, goal):
#         self.advice = advice
#         self.further = further
#         self.backward = backward
#         self.goal = goal

#     def createSolution(self):
#         prompt = (f'How can I accomplish {self.goal}')
#         message =  [{"role": "user", "content": f"{prompt}"}]
#         try:
#             response =openai.ChatCompletion.create(model="gpt-4",
#                                  messages=[message])
#         except:
#             pass

async def createSolution(goal):
    prompt = (f'How can I accomplish {goal}')
    message =  [{"role": "user", "content": f"{prompt}"}]
    try:
        response =openai.ChatCompletion.create(model="gpt-4",
                                messages=[
                                        {"role": "user", "content": prompt}])
    except:
        pass
    text = response["choices"][0]["message"]["content"]
    return text

async def createTasks(solution):
    tasks = []
    prompt = (f"Giventhe following, create numbered tasks to accomplish this {solution}")
    message =  [{"role": "user", "content": f"{prompt}"}]
    try:
        response = openai.ChatCompletion.create(model="gpt-4",
                                messages=[
                                        {"role": "user", "content": prompt}])
    except:
        pass
    text = response["choices"][0]["message"]["content"]

    print(text)

    for task  in text.split('\n'):
        task.strip()
        tasks.append(task)
    return tasks
        

async def categorize(thing_list):
    categories = []
    prompt= (f"Create categories based on the items in this list: {thing_list}. seperate each category with a line")
    message =  [{"role": "user", "content": f"{prompt}"}]
    try:
        response = openai.ChatCompletion.create(model="gpt-4",
                                messages=[
                                        {"role": "user", "content": prompt}])
    except:
        pass
    text = response["choices"][0]["message"]["content"]

    print(text)

    for section in text.split('\n'):
        section.strip()
        print(section)
        categories.append(section)
    return(categories)







        
