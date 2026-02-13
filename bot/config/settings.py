import os

from dotenv import load_dotenv

load_dotenv()

class Settings:
    BOT_TOKEN: str = os.getenv("BOT_TOKEN")
    GEMINI_API_KEY: str = os.getenv("GEMINI_API_KEY")

settings = Settings()