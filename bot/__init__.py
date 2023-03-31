from pyrogram import Client
from pyrogram.types import User
from bot.utils import watchlog
from bot import config
from typing import Union, Optional
from shroudapi import ShroudAPI

opt = config.load()


class Bot(Client):
    _instance: Union[None, "Bot"] = None

    me: Optional[User] = None
    shroud: ShroudAPI = ShroudAPI(opt.shroud.email, opt.shroud.password, opt.shroud.totp)

    def __init__(self, inst_name: str = 'daemon'):
        super().__init__(
            inst_name,
            api_id=opt.bot.api_id,
            api_hash=opt.bot.api_hash,
            bot_token=opt.bot.bot_token,
            plugins=dict(root='bot/plugins')
        )

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    async def shroud_auth(self):
        await self.shroud.auth()

    @property
    def admins(self):
        return [525239263]

    def start_serve(self):
        self.start()
        self.me = self.get_me()
        self.stop()
        self.session.MAX_RETRIES = 1
        print('listening on', self.me.first_name, '@'+self.me.username)
        self.run()
