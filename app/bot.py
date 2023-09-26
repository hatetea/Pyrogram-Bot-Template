from pyrogram import Client, __version__
from pyrogram.raw.all import layer
from app import (
    APP_ID,
    API_HASH,
    BOT_TOKEN,
    LOGGER
)

class Denyska(Client):

    def __init__(self):
        # name = self.__class__.__name__.lower()
        super().__init__(
            name="Denyska",
            plugins=dict(root=f"app/plugins"),
            api_id=APP_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            in_memory=True
        )

    async def start(self):
        await super().start()
        usr_bot_me = self.me
        LOGGER.info(
            f"Denyska based on Pyrogram v{__version__} "
            f"(Layer {layer}) started on @{usr_bot_me.username}. "
            "hi. im in love with Denys"
        )

    async def stop(self):
        await super().stop()
        LOGGER.info("Bot stopped. Bye.")

    