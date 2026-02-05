# chain of thought prompting

from dotenv import load_dotenv
from openai import OpenAI
import os
import json
import requests

load_dotenv()

client = OpenAI(
    api_key = os.getenv("GOOGLE_API_KEY"),
    base_url = "https://generativelanguage.googleapis.com/v1beta/"
)



def get_weather(city: str):
    try:
        # Step 1: Get latitude & longitude by city name
        geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}"
        geo_response = requests.get(geo_url)
        geo_data = geo_response.json()

        # If city not found
        if "results" not in geo_data or len(geo_data["results"]) == 0:
            return f"Sorry, I could not find the city '{city}'."

        # Take the first matching result
        latitude = geo_data["results"][0]["latitude"]
        longitude = geo_data["results"][0]["longitude"]

        # Step 2: Get current weather using coordinates
        weather_url = (
            f"https://api.open-meteo.com/v1/forecast?"
            f"latitude={latitude}&longitude={longitude}&current_weather=true"
        )
        weather_response = requests.get(weather_url)
        weather_data = weather_response.json()

        if "current_weather" not in weather_data:
            return f"Weather data for '{city}' is currently unavailable."

        # Extract weather info
        current = weather_data["current_weather"]
        temp = current["temperature"]
        windspeed = current["windspeed"]
        wind_dir = current["winddirection"]
        code = current["weathercode"]
        time = current["time"]

        # Format final message
        return (
            f"The weather in {city.capitalize()} is {temp}°C with a windspeed of "
            f"{windspeed} km/h, wind direction {wind_dir}°, and weather code {code}. "
            f"(Updated at {time})"
        )

    except Exception as e:
        return f"Error fetching weather: {str(e)}"
    


available_tools = {
    "get_weather": get_weather
}    




SYSTEM_PROMPT = """
    You're an expert AI Assistant in resolving user queries using chain of thought.
    You work on START, PLAN AND OUTPUT steps.
    You need to first PLAN what needs to done. The PLAN can be multiple steps.
    Once you think enough PLAN has been done, finally you can give an OUTPUT.
    You can also call a tool if required from the list of available tools.
    for every tool call wait for the observe step which is the output of the called tool.

    Rules:
    - Strictly Follow the given JSON output format.
    - Output ONLY ONE JSON object per turn. Do not wrap it in a list [].
    - Only run one step at a time.
    - The sequence of steps is START (where user give an input), PLAN(That can be multiple times) and finally OUTPUT (which is going to displayed to the user)

    Output JSON Format:
        {"step": "START" | "PLAN" | "OUTPUT" | "TOOL", "content": "string", "tool": "string", "input": "string"}

    Available Tools:
    - get_weather: Takes city name as an input string and returns the weather info about the city.

    Example 1:
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


    Example 2:
    Q: what is the weather of Delhi ? 
    PLAN: {"step": "PLAN", "content": "seems like user is interested in getting weather of Delhi in India"}
    PLAN: {"step": "PLAN", "content": "Lets see if we have any available tool from the list of available tools"}
    PLAN: {"step": "PLAN", "content": "Great, we have get_weather tool available tool for this query."}
    PLAN: {"step": "PLAN", "content": "I need to call get_weather tool for delhi as input for city"}
    PLAN: {"step": "TOOL", "tool": "get_weather", "content": "delhi"}
    PLAN: {"step": "OBSERVE", "tool": "get_weather", "output": "The temperature of delhi is cloudy with 20 c"}
    PLAN: {"step": "PLAN", "content": "I got the weather info about delhi"}
    OUTPUT: {"step": "OUTPUT", "content": "The current weather in delhi is 20 C with some cloudy sky"}


"""

print("\n\n\n")

message_history = [
     {
            "role":"system",
            "content":SYSTEM_PROMPT
     },
]

while True:
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

        if isinstance(parsed_result, list):
            parsed_result = parsed_result[0]

        if parsed_result.get("step") == "START":
            print("🔥", parsed_result.get("content"))
            continue

        if parsed_result.get("step") == "TOOL":
            tool_to_call = parsed_result.get("tool")
            tool_input = parsed_result.get("input")
            print(f"🛠️: {tool_to_call} ({tool_input})")

            tool_response = available_tools[tool_to_call](tool_input)
            message_history.append({"role":"developer", "content": json.dumps(
                {"step": "OBSERVE", "tool":tool_to_call, "input":tool_input, "output": tool_response}
            )})
            continue
        
        if parsed_result.get("step") == "PLAN":
            print("🧠", parsed_result.get("content"))
            continue

        if parsed_result.get("step") == "OUTPUT":
            print("🤖", parsed_result.get("content"))
            break


print("\n\n\n")