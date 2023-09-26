# needed to appropriately, select ENV vars / Config vars
import os

# the logging things
import logging

from app.config import Config


logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


# TODO: is there a better way?
LOGGER = logging.getLogger(__name__)
APP_ID = Config.APP_ID
API_HASH = Config.API_HASH
BOT_TOKEN = Config.BOT_TOKEN