# Persona Based Prompting 

from dotenv import load_dotenv
from openai import OpenAI
import os
import json

load_dotenv()

client = OpenAI(
    api_key = os.getenv("GOOGLE_API_KEY"),
    base_url = "https://generativelanguage.googleapis.com/v1beta/"
)

SYSTEM_PROMPT = """
    You are an AI Persona Assistant named Piyush Gard.
    You are acting on behalf of Piyush Garg who is 25 years old Tech enthusiatic and principle engineer.Your main tech stack is JS and Python 
    and you are learning GenAI these days.

    Examples:
    Q: Hey
    A: Hey, What's up!
"""

response = client.chat.completions.create(
        model = "gemini-3-flash-preview",
        messages = [
            {
                "role":"system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": "Hey There"
            }
        ]
    )


print("Response: ", response.choices[0].message.content)