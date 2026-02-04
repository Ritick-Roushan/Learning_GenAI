
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
            "role":"user",
            "content":"Hey, I am Ritick. Nice to meet you "
        }
    ]
)

print(response.choices[0].message.content)












# this is how we set up for openai

# from dotenv import load_dotenv
# from openai import OpenAI

# load_dotenv()

# client = OpenAI()

# response = client.chat.completions.create(
#     model = "gpt-4o-mini",
#     messages = [
#         {
#             "role":"user",
#             "content":"Hey, I am Ritick. Nice to meet you "
#         }
#     ]
# )

# print(response.choices[0].message.content)