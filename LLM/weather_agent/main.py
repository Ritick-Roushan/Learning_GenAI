from openai import OpenAI
from dotenv import load_dotenv
import os
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
    


def main():
    user_query = input(">")

    response = client.chat.completions.create(
        model = "gemini-3-flash-preview",
        messages = [
            {
                "role" : "user",
                "content" : user_query
            }
        ]
    )

    print(f"🤖:{response.choices[0].message.content}")

main()  