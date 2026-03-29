from openai import OpenAI
import json
client = OpenAI()   

class MultiTools:
    def __init__(self):
        self.tools = {}
    def get_weather_detail(self, city):
            return {"city": city, "temperature": 30}
    def convert_to_fahrenheit(self, temp):
            return (temp * 9/5) + 32
    def call_tool(self, prompt):

        
        # -------- TOOL SCHEMA --------

        tools = [
            {
                "type": "function",
                "function": {
                    "name": "get_weather",
                    "description": "Get temperature of a city in Celsius",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "city": {"type": "string"}
                        },
                        "required": ["city"]
                    }
                }
            },
            {
                "type": "function",
                "function": {
                    "name": "convert_to_fahrenheit",
                    "description": "Convert Celsius to Fahrenheit",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "temp": {"type": "number"}
                        },
                        "required": ["temp"]
                    }
                }
            }
        ]
        # -------- USER QUESTION --------

        messages = [
            {"role": "system", "content": "You are a helpful assistant that can call tools to get weather information and convert temperatures."},
            {"role": "user", "content": prompt}
        ]
        # -------- MODEL RESPONSE --------

        response = client.chat.completions.create(
            model="gpt-5",
            messages=messages,
            tools=tools
        )

        # Safely extract tool call (model may return content instead)
        msg = response.choices[0].message
        tool_calls = getattr(msg, "tool_calls", None)

        if not tool_calls:
            content = getattr(msg, "content", None)
            if content:
                return content
            return "No tool call returned by the model."

        tool_call = tool_calls[0]

        name = tool_call.function.name
        args = json.loads(tool_call.function.arguments)
        
        # -------- EXECUTE FIRST TOOL --------

        if name == "get_weather":
            result = self.get_weather_detail(**args)

        # Add tool result to conversation
        messages.append(response.choices[0].message)

        messages.append({
            "role": "tool",
            "tool_call_id": tool_call.id,
            "content": json.dumps(result)
        })
        # -------- SECOND TOOL CALL --------

        response2 = client.chat.completions.create(
            model="gpt-5",
            messages=messages,
            tools=tools
        )

        # Safely extract second tool call
        msg2 = response2.choices[0].message
        tool_calls2 = getattr(msg2, "tool_calls", None)

        if not tool_calls2:
            content2 = getattr(msg2, "content", None)
            if content2:
                return content2
            return "No second tool call returned by the model."

        tool_call2 = tool_calls2[0]

        name2 = tool_call2.function.name
        args2 = json.loads(tool_call2.function.arguments)

        if name2 == "convert_to_fahrenheit":
            result2 = self.convert_to_fahrenheit(**args2)

        messages.append(response2.choices[0].message)

        messages.append({
            "role": "tool",
            "tool_call_id": tool_call2.id,
            "content": str(result2)
        })
        # -------- FINAL RESPONSE --------

        final = client.chat.completions.create(
            model="gpt-5",
            messages=messages
        )

        return final.choices[0].message.content