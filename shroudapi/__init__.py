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

            resp = await session.post(self.url + '/token', json=data)
            if resp.status != 200:
                raise errors.AuthError('Email or Password is incorrect.')

            self.token: types.Token = types.Token.from_json(await resp.text())
            headers = {'Authorization': f'Bearer {self.token.token}'}
            self.session = aiohttp.ClientSession(headers=headers)
            return self.token

    async def aliases(self, page_size: int = 20, pages: int = 1):
        async with self.session as session:
            # ?page_size=10&page=3
            resp = await session.get(self.url + f'/aliases?page_size={page_size}&page={pages}')
            if resp.status != 200:
                raise errors.AliasError('Request Alias Error.')
            return types.Alias.from_json(await resp.text())

    async def create(self, alias: str = None, domain: str = None):
        custom_domain = bool(alias) is True and bool(domain) is True
        if not bool(alias) == bool(domain):
            raise errors.CreateAliasError('You must specify either an alias or a domain.')

        data: dict = None
        async with self.session as session:
            if custom_domain:
                data = {
                    'local_part': alias,
                    'domain': domain
                }
            resp = await session.post(self.url + '/aliases', json=data)
            if resp.status != 200:
                try:
                    raise errors.CreateAliasError((await resp.json())['error'])
                except Exception:
                    raise errors.CreateAliasError('Request to create new alias error.')
            return types.EmailAliases.from_json(await resp.text())
