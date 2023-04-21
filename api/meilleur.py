import openai
import os
from dotenv import load_dotenv
import asyncio


load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

class Guide:
    def __init__(self, prompt,advice, further, backward, goal):
        self.prompt = prompt
        self.advice = advice
        self.further = further
        self.backward = backward
        self.goal = goal

    # def goal(self):

        
