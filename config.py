import os

class Config:
    # Telegram API Credentials
    API_ID = int(os.environ.get("API_ID", "12345678"))
    API_HASH = os.environ.get("API_HASH", "your_api_hash_here")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "your_bot_token_here")

