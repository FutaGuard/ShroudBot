from pyrogram import Client, filters
from bot import config, Bot
from shroudapi.types import EmailAliases

opt = config.load()


@Client.on_message(filters.command('gen') & filters.user(opt.admin))
async def gen(client: Bot, message):
    """
    Generate a new alias with random string
    """
    await client.shroud_auth()
    # await client.shroud.auth()
    new: EmailAliases = await client.shroud.create()
    text = '✨ 已成功建立一個新的別名\n' \
           '`{alias}`\n'.format(
            alias=new.address)

    await message.reply_text(text)
