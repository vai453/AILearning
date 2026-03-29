from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("API_KEY_GEMINI") or os.getenv("OPENAI_API_KEY")
if not API_KEY:
    raise RuntimeError("Set API_KEY_GEMINI or OPENAI_API_KEY in your environment or .env file")

client = OpenAI(api_key=API_KEY, base_url="https://generativelanguage.googleapis.com/v1beta/openai/")

class TextGeneration:
    def __init__(self, model="gemini-3-flash-preview"):
        self.model = model

    def generate_text(self, prompt):
        response = client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content
    
    def generate_text_with_instructions(self, prompt):
        response = client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": "You are a helpful assistant. Talk like a Math tutor."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )
        return response.choices[0].message.content