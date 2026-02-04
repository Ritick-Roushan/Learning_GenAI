from google import genai
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

# Read key from environment variable
api_key = os.getenv("GOOGLE_API_KEY")

client = genai.Client(api_key=api_key)

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=[
        {
            "role": "user",
            "parts": [
                {"text": "Hey, I am Bhardwaz, Nice to meet you"}
            ]
        }
    ]
)

print(response.text)
