import os

from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

openai = OpenAI()

class FewChatBot:
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
                        
                    Classify some common diseases based on symptoms. For example:
                    - If the user says "I have a fever and cough", reply with "You might have the flu."
                    - If the user says "I have a headache and sensitivity to light", reply with "You might have a migraine."
                    - If the user says "I have chest pain and shortness of breath", reply with "You might have a heart attack."
                    - If the user says "I have a sore throat and runny nose", reply with "You might have a common cold."
                    - If the user says "I have joint pain and stiffness", reply with "You might have arthritis."
                    - If the user says "I have abdominal pain and diarrhea", reply with "You might have food poisoning."
                    - If the user says "I have fatigue and weight loss", reply with "You might have diabetes."
                    - If the user says "I have a rash and itching", reply with "You might have an allergic reaction."
                        
                        """
                    )
                },
                {"role": "user", "content": user_input}
            ],
            temperature=0.3
        )
        return response.choices[0].message.content.strip()