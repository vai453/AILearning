from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()

class TextGeneration:
    def __init__(self, model="gpt-5"):
        self.model = model

    def generate_text(self,prompt):
        response = client.responses.create(
        model=self.model,
        input=prompt)

        return response.output_text
    
    def generate_text_with_instructions(self, prompt):
        response = client.responses.create(
                model=self.model,
                reasoning={"effort": "low"},
                instructions="Talk like a Math tutor.",
                input=prompt,
            
        )
        return response.output_text