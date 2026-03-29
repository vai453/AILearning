from openai import OpenAI
# from dotenv import load_dotenv
import os
# load_dotenv()

# client = OpenAI()

# API_KEY = os.getenv("API_KEY_GEMINI");
API_KEY = "AIzaSyDv_tuNFXzIBccfvTV5RAELj0KtY6r6sfk"
client=OpenAI(api_key=API_KEY,base_url="https://generativelanguage.googleapis.com/v1beta/openai/")

class ChatBot:
    def __init__(self, name):
        self.name = name
        # self.model="gpt-4o"
        self.model="gemini-3-flash-preview"

    def send_message(self, message):
        response = client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": f"You are a helpful assistant named {self.name}. You are Maths mentor only. You have to give the Maths related Answer otherwise you have to say that you are a Maths mentor and you can't answer non-Maths related questions."},
                {"role": "user", "content": message}
            ]
        )
        return response.choices[0].message.content