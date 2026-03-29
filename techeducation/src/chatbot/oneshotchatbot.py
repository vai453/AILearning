import os

from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

openai = OpenAI()

class OneChatBot:
    def __init__(self):
        load_dotenv()
        self.model = "gpt-4o-mini"
    
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