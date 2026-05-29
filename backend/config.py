import os

# LM Studio Server configuration
LM_STUDIO_BASE_URL = os.getenv("LM_STUDIO_BASE_URL", "http://127.0.0.1:1234/v1")
MODEL_NAME = os.getenv("MODEL_NAME", "google/gemma-4-e4b:2")

# Server settings
HOST = "127.0.0.1"
PORT = 8000
