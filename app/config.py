import os
from dotenv import load_dotenv



load_dotenv("config.env")


class Config:
    LOGGER = True
    APP_ID = int(os.environ.get("API_ID"))
    API_HASH = os.environ.get("API_HASH")
    BOT_TOKEN = os.environ.get("BOT_TOKEN")
    


class Production(Config):
    LOGGER = False


class Development(Config):
    LOGGER = True