
from asyncio import tools
import json
import os
import requests

from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()
API_KEY=os.getenv("OPENWEATHER_API_KEY")
client = OpenAI()

class WheatherFunctionChatbot:
    def __init__(self):
        self.model = "gpt-5"

    def get_wheather_detail(self, user_input):
        # def get_weather(city):
        #     return f"The weather in {city} is 28°C"
        def get_weather(city):
            url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    
            response = requests.get(url)
            data = response.json()
            print(data)
            if response.status_code == 200:
                temperature = data["main"]["temp"]
                description = data["weather"][0]["description"]
                country = data["sys"]["country"]

                return f"Temperature in {city}, {country} is {temperature}°C with {description}"
            
            else:
                return "City not found"
        result = None
        # Tool (function) schema
        tools = [
            {
                "type": "function",
                "function": {
                    "name": "get_weather",
                    "description": "Get the weather information for a city",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "city": {
                                "type": "string",
                                "description": "Name of the city"
                            }
                        },
                        "required": ["city"]
                    }
                }
            }
        ]
        # Send request to LLM
        response = client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": user_input}],
            tools=tools
        )
        # Extract tool call (guard against missing tool_calls)
        msg = response.choices[0].message
        tool_calls = getattr(msg, "tool_calls", None)

        if not tool_calls:
            # Fall back to returned content if model didn't call the tool
            content = getattr(msg, "content", None)
            if content:
                return content
            return "No tool call returned by the model."

        tool_call = tool_calls[0]
        function_name = tool_call.function.name
        arguments = json.loads(tool_call.function.arguments)

        # Execute function
        if function_name == "get_weather":
            result = get_weather(arguments["city"])

        return result
        
