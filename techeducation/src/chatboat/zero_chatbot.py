import os

from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

openai = OpenAI(
    api_key="AIzaSyDJz0UpjyJ915J3vu6gdMuwnZU1DA_Dlpo",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

class ZeroChatBot:
    def __init__(self):
        load_dotenv()
        # self.model = "gpt-4o-mini"
        self.model = "gemini-3-flash-preview"
    
    def generate_response(self, user_input):
        # fallback to AI assistant for other medical queries
        response = openai.chat.completions.create(
            model=self.model,
            messages=[
                {
                    "role": "system",
                    "content": """You are a helpful medical assistant. Please classify some common diseases based on symptoms. 
                    Please give the answer of the health related question. If the question is not health related, reply exactly with: 'I am sorry, I can only answer health related questions.'
                    """
                },
                {"role": "user", "content": user_input}
            ],
            temperature=0.3
        )
        return response.choices[0].message.content.strip()