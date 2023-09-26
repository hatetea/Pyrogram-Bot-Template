from pyrogram import filters, types
from app.bot import Denyska as app

start_message = '**🔥 я дениска и я оч красивый мальчик Uwuuu <333 kawaii**'

async def get_start(message) -> types.Message:
    await message.reply(start_message)

@app.on_message(filters.command(['start', 'ты кто'], prefixes=['!', '/', '']))
async def new_welcome(_, message):
    await get_start(message)
    