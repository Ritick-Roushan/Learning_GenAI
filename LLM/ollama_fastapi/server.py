from fastapi import FastAPI, Body
from ollama import Client

app = FastAPI()
client = Client(
    host = "http://localhost:11434/"
)

@app.get("/")
def read_root():
    return {"name":"Bhardwaz"}

@app.get("/contact-us")
def read_root():
    return {"email":"ritickbhardwaz630@gmail.com"}

@app.post("/chat")
def chat(
        message: str = Body(..., description = "The Message")
):
    response = client.chat(model = "gemma3:1b", messages=[
        {
            "role": "user",
            "content": message
        }
    ])

    return {"response": response.message.content}
