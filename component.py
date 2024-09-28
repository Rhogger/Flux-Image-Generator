from langflow.custom import Component
from langflow.inputs import MessageTextInput
from langflow.template import Output
from langflow.schema import Data
import requests

class FluxImageGeneratorComponent(Component):
    display_name = "Image Generator with Auth"
    description = "Generates an image from the Flux.dev API using a prompt and API key for authentication."
    icon = "image"

    inputs = [
        MessageTextInput(
            name="input_prompt",
            display_name="Image Prompt",
            info="Describe the image you want to generate.",
        ),
        MessageTextInput(
            name="api_key",
            display_name="API Key",
            info="Your API key for authentication. Generate from fal.ai."
        )
    ]

    outputs = [
        Output(display_name="Image URL", name="image_url", method="generate_image"),
    ]

    def generate_image(self) -> Data:
        prompt = self.input_prompt
        api_key = self.api_key

        url = "https://fal.run/fal-ai/flux/dev"

        headers = {
            "Authorization": f"Key {api_key}",
            "Content-Type": "application/json"
        }

        data = {
            "prompt": prompt
        }

        response = requests.post(url, json=data, headers=headers)

        if response.status_code == 200:
            response_data = response.json()
            request_id = response_data.get("request_id", "")

            image_url = response_data.get("images", [{}])[0].get("url", "")

            return Data(data={"image_url": image_url})
        else:
            return Data(data={"error": f"Failed to generate image: {response.text}"})
