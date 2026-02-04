# zero shot prompting

from dotenv import load_dotenv
from openai import OpenAI
import os

load_dotenv()

client = OpenAI(
    api_key = os.getenv("GOOGLE_API_KEY"),
    base_url = "https://generativelanguage.googleapis.com/v1beta/"
)

# zero shot prompting: directly giving the instruction to the model

SYSTEM_PROMPT = "you should answer only and only coding related questions. Do not answer antything else. Your name is Alexa. If user asks something is other than coding just say sorry"

response = client.chat.completions.create(
    model = "gemini-3-flash-preview",
    messages = [
        {
            "role":"system",
            "content":SYSTEM_PROMPT
        },
        {
            "role":"user",
            "content":"Hey, can you give me code of python of adding two numbers "
        }
    ]
)

print(response.choices[0].message.content)
