# chain of thought prompting, in this instead of doing manual chaining which we did in earlier in this we do automatic chaining 

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
    You're an expert AI Assistant in resolving user queries using chain of thought.
    You work on START, PLAN AND OUTPUT steps.
    You need to first PLAN what needs to done. The PLAN can be multiple steps.
    Once you think enough PLAN has been done, finally you can give an OUTPUT.

    Rules:
    - Strictly Follow the given JSON output format.
    - Only run one step at a time.
    - The sequence of steps is START (where user give an input), PLAN(That can be multiple times) and finally OUTPUT (which is going to displayed to the user)

    Output JSON Format:
        {"step": "START" | "PLAN" | "OUTPUT", "content": "string"}

    Example:
    Q: Hey, can you solve 2 + 3 * 5 / 10
    PLAN: {"step": "PLAN", "content": "seems like user is interested in math problem"}
    PLAN: {"step": "PLAN", "content": "looking at the problem, we should resolve this using BODMAS method"}
    PLAN: {"step": "PLAN", "content": "Yes The Bodmas is correct thing to be done here"}
    PLAN: {"step": "PLAN", "content": "first we must multiply 3 * 5 whihc is 15"}
    PLAN: {"step": "PLAN", "content": "Now the new equation is 2 + 15 / 10"}
    PLAN: {"step": "PLAN", "content": "we must perform divide that is 15 / 10 = 1.5"}
    PLAN: {"step": "PLAN", "content": "Now the equation is 2 + 1.5"}
    PLAN: {"step": "PLAN", "content": "Now finally lets perform the add 3.5"}
    PLAN: {"step": "PLAN", "content": "Great, we have solved and finally left with 3.5 as ans"}
    OUTPUT: {"step": "OUTPUT", "content": "3.5"}


"""

print("\n\n\n")

message_history = [
     {
            "role":"system",
            "content":SYSTEM_PROMPT
     },
]

user_query = input("👉")

message_history.append({"role":"user", "content": user_query})

while True:
    response = client.chat.completions.create(
        model = "gemini-3-flash-preview",
        response_format = {"type": "json_object"},
        messages = message_history
    )

    raw_result = (response.choices[0].message.content)
    message_history.append({"role":"assistant", "content": raw_result})
    parsed_result = json.loads(raw_result)

    if parsed_result.get("step") == "START":
        print("🔥", parsed_result.get("content"))
        continue
    
    if parsed_result.get("step") == "PLAN":
        print("🧠", parsed_result.get("content"))
        continue

    if parsed_result.get("step") == "OUTPUT":
        print("🤖", parsed_result.get("content"))
        break


print("\n\n\n")