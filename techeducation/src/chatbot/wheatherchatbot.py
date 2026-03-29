from openai import OpenAI
import json

client = OpenAI()

class WheaterChatbot:
        def __init__(self, model: str = "gpt-4o-mini"):
                self.model = model

        def get_wheather_detail(self, location: str):
                """Return weather details for `location` using the chat API.

                Tries to parse a JSON response from the model. If parsing fails,
                returns the raw text returned by the model.
                """
                prompt_system = (
                        "You are a helpful weather assistant. Provide concise current weather "
                        "details and a short 2-day forecast for the requested location. "
                        "Return the answer as JSON with keys: `location`, `temperature_c`, "
                        "`condition`, `humidity`, `wind_kph`, and `forecast` (list of day-summary objects)."
                )

                response = client.chat.completions.create(
                        model=self.model,
                        messages=[
                                {"role": "system", "content": prompt_system},
                                {"role": "user", "content": f"Get weather for: {location}"},
                        ],
                        temperature=0.0,
                )

                text = response.choices[0].message.content
                try:
                        return json.loads(text)
                except Exception:
                        return text

