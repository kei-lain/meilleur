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





        
