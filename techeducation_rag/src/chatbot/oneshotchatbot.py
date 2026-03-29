import os

from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()
API_KEY = os.getenv("API_KEY_GEMINI") or os.getenv("OPENAI_API_KEY")
if not API_KEY:
    raise RuntimeError("Set API_KEY_GEMINI or OPENAI_API_KEY in your environment or .env file")

openai = OpenAI(api_key=API_KEY, base_url="https://generativelanguage.googleapis.com/v1beta/openai/")

class OneChatBot:
    def __init__(self):
        load_dotenv()
        self.model = "gemini-3-flash-preview"
    
    def generate_response(self, user_input):
        # fallback to AI assistant for other medical queries
        response = openai.chat.completions.create(
            model=self.model,
            messages=[
                {
                    "role": "system",
                    "content": (
                        """You are a helpful medical assistant. Please classify some common diseases based on symptoms. 
                        If get any non-medical query, reply with "Sorry, I am a medical assistant and I can only answer medical related questions."
                    Classify some common diseases based on symptoms. For example:
                    - If the user says "I have a fever and cough", reply with "You might have the flu."  
                        """
                    )
                },
                {"role": "user", "content": user_input}
            ],
            temperature=0.3
        )
        return response.choices[0].message.content.strip()