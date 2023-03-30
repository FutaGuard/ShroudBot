from pyrogram import Client, filters


@Client.on_message(filters.command('ping'))
async def ping(client, message):
    await message.reply_text('pong')