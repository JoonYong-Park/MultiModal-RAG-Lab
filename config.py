import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
UPSTAGE_API_KEY = os.getenv("UPSTAGE_API_KEY")
COHERE_API_KEY = os.getenv("COHERE_API_KEY")