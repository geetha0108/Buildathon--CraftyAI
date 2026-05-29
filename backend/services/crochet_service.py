import base64
import json
import re
import logging
from typing import Optional, Dict, Any

from fastapi import UploadFile
from openai import OpenAI

from config import LM_STUDIO_BASE_URL, MODEL_NAME

logger = logging.getLogger("crochet_service")
logging.basicConfig(level=logging.INFO)

# LM Studio OpenAI-compatible client
client = OpenAI(
    base_url=LM_STUDIO_BASE_URL,
    api_key="lm-studio"
)

class CrochetService:

    @staticmethod
    async def encode_image(image: UploadFile) -> str:
        """
        Reads the uploaded image and converts it to base64 data URL.
        """

        content = await image.read()

        encoded = base64.b64encode(content).decode("utf-8")

        mime_type = image.content_type or "image/jpeg"

        await image.seek(0)

        return f"data:{mime_type};base64,{encoded}"

    @classmethod
    async def generate_pattern(
        cls,
        prompt: str,
        image: Optional[UploadFile] = None
    ) -> Dict[str, Any]:

        system_prompt = (
            "You are a professional expert AI crochet pattern generator.\n"
            "Generate a beautiful crochet pattern.\n"
            "Respond ONLY with valid JSON.\n\n"

            "Required JSON format:\n"

            "{\n"
            '  "project_title": "Crochet project name",\n'
            '  "materials": ["list of materials"],\n'
            '  "yarn_colors": ["recommended colors"],\n'
            '  "hook_size": "recommended hook size",\n'
            '  "difficulty": "Beginner/Easy/Intermediate/Advanced",\n'
            '  "crochet_instructions": ["step-by-step instructions"],\n'
            '  "finishing_tips": ["finishing tips"]\n'
            "}"
        )

        user_text = (
            f"Generate a crochet pattern for: {prompt}"
        )

        # Multimodal message
        if image:

            try:
                base64_data = await cls.encode_image(image)

                user_content = [
                    {
                        "type": "text",
                        "text": user_text
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": base64_data
                        }
                    }
                ]

                logger.info("Image encoded successfully.")

            except Exception as e:

                logger.error(f"Image encoding failed: {str(e)}")

                user_content = user_text

        else:
            user_content = user_text

        try:

            print("LM Studio URL:", LM_STUDIO_BASE_URL)
            print("Model:", MODEL_NAME)

            response = client.chat.completions.create(

                model=MODEL_NAME,

                messages=[
                    {
                        "role": "system",
                        "content": system_prompt
                    },
                    {
                        "role": "user",
                        "content": user_content
                    }
                ],

                temperature=0.7

            )

            content = response.choices[0].message.content

            logger.info(
                f"Received response from LM Studio: {content[:200]}..."
            )

            return cls._parse_and_validate_json(content)

        except Exception as e:

            logger.error(f"LM Studio error: {str(e)}")

            raise Exception(
                f"LM Studio connection failed: {str(e)}"
            )

    @classmethod
    def _parse_and_validate_json(
        cls,
        raw_content: str
    ) -> Dict[str, Any]:

        cleaned = raw_content.strip()

        # Remove markdown wrappers
        if cleaned.startswith("```"):

            cleaned = re.sub(
                r"^```(?:json)?\s*",
                "",
                cleaned
            )

            cleaned = re.sub(
                r"\s*```$",
                "",
                cleaned
            )

            cleaned = cleaned.strip()

        try:

            parsed = json.loads(cleaned)

        except json.JSONDecodeError:

            match = re.search(
                r"(\{.*\})",
                cleaned,
                re.DOTALL
            )

            if match:

                try:
                    parsed = json.loads(match.group(1))

                except json.JSONDecodeError:

                    raise Exception(
                        "Failed to parse generated JSON."
                    )

            else:

                raise Exception(
                    "No valid JSON found in model response."
                )

        required_keys = {

            "project_title":
                "Custom Crochet Project",

            "materials":
                ["Standard crochet supplies"],

            "yarn_colors":
                ["Pastel Colors"],

            "hook_size":
                "4.0mm",

            "difficulty":
                "Intermediate",

            "crochet_instructions":
                ["Instructions could not be generated."],

            "finishing_tips":
                ["Weave in loose ends carefully."]
        }

        final_response = {}

        for key, default in required_keys.items():

            value = parsed.get(key)

            if value is None:

                final_response[key] = default

            elif isinstance(default, list):

                if isinstance(value, list):

                    final_response[key] = [
                        str(v) for v in value
                    ]

                else:

                    final_response[key] = [str(value)]

            else:

                final_response[key] = str(value)

        return final_response