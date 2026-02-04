from dotenv import load_dotenv
from openai import OpenAI
import os

load_dotenv()

client = OpenAI(
    api_key = os.getenv("GOOGLE_API_KEY"),
    base_url = "https://generativelanguage.googleapis.com/v1beta/"
)

response = client.chat.completions.create(
    model = "gemini-3-flash-preview",
    messages = [
        {
            "role":"system",
            "content":"You are expert in Maths and answer only ans only maths related question. If query is not related with maths say sorry and not answer"
        },
        {
            "role":"user",
            "content":"Hey, can you write a code in python to print Hello"
        }
    ]
)

print(response.choices[0].message.content)
