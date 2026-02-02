import os

API_KEY = os.getenv("SAMBANOVA_API_KEY")
BASE_URL = "https://api.sambanova.ai/v1"
MODEL_NAME = "DeepSeek-V3.1"


# DO NOT CRASH — just warn
if not API_KEY:
    print(" WARNING: SAMBANOVA_API_KEY is missing")
