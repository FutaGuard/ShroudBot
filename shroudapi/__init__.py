import aiohttp
from typing import Optional
from shroudapi import errors, types


class ShroudAPI:
    def __init__(self, email: str, password: str, totp: Optional[str] = None):
        self.session: aiohttp.ClientSession() = None
        self.url: str = 'https://app.shroud.email/api/v1'
        self.email: str = email
        self.password: str = password
        self.totp: str = totp
        self.token: types.Token = None

    async def auth(self) -> types.Token:
        async with aiohttp.ClientSession() as session:
            data = {
                'email': self.email,
                'password': self.password,
            }
            if self.totp:
                data['totp'] = self.totp

            resp = await session.post(f'{self.url}/token', json=data)
            if resp.status != 200:
                raise errors.AuthError('Email or Password is incorrect.')

            self.token: types.Token = types.Token.from_json(await resp.text())
            headers = {'Authorization': f'Bearer {self.token.token}'}
            self.session = aiohttp.ClientSession(headers=headers)
            return self.token

    async def list(self, pages: int = 1):
        async with self.session as session:
            resp = await session.get(f'{self.url}/aliases')
            print(await resp.text())

