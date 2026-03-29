from openai import OpenAI
import base64

from http import client


client = OpenAI() 


class ImageGenChatBot:
    def __init__(self, openai_client):
        self.openai = openai_client

    def generate_image(self, prompt):
        response = client.responses.create(
            model="gpt-4.1-mini",
            input=prompt,
            tools=[{"type": "image_generation"}],
        )

        # Save the image to a file
        image_data = [
            output.result
            for output in response.output
            if output.type == "image_generation_call"
        ]

        if image_data:
            image_base64 = image_data[0]
            with open("cat_and_otter.png", "wb") as f:
                f.write(base64.b64decode(image_base64))