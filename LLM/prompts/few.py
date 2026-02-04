# Few shot prompting

from dotenv import load_dotenv
from openai import OpenAI
import os

load_dotenv()

client = OpenAI(
    api_key = os.getenv("GOOGLE_API_KEY"),
    base_url = "https://generativelanguage.googleapis.com/v1beta/"
)

# Few shot prompting: the model is provided with a few examples before asking it to generate a response.

SYSTEM_PROMPT = """
you should answer only and only coding related questions. Do not answer antything else. Your name is Alexa. If user asks something is other than coding just say sorry.

Rule:
 - Strictly follow the output in JSON format

Output format:
 {{
 "code": "String" or null,
 "isCodingQuestion": boolean
 }} 

 Examples:
 Q:Can you explain the a+b whole squre?
 A: {{"code": null, "iscodingQuestion": false}}

 Q: Hey , write a code in python for adding two numbers.
 A: {{"code": "def (a,b):
         return a + b" , "iscodingQuestion": false}}




# Examples:
# Q: Can you explain the a+b whole squre?
# A: Sorry, I can only help with coding related questions.

# Q: Hey , write a code in python for adding two numbers.
# A: def (a,b):
#        return a + b

"""

response = client.chat.completions.create(
    model = "gemini-3-flash-preview",
    messages = [
        {
            "role":"system",
            "content":SYSTEM_PROMPT
        },
        {
            "role":"user",
            "content":"Hey , write a code in python for adding two numbers."
        }
    ]
)

print(response.choices[0].message.content)
