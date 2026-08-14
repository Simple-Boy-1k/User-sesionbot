import os

class Config:
    # Telegram API Credentials (my.telegram.org se milega)
    # Agar environment variable set nahi hoga, toh default value None rhegi
    API_ID = int(os.environ.get("API_ID", "0"))
    API_HASH = os.environ.get("API_HASH", "")
    
    # Bot Token (@BotFather se milega)
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
