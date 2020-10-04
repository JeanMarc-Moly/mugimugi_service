from httpx import AsyncClient

from ..abstract import Client


class AsynchronousClient(Client):
    async def query(self, **kwargs):
        return await self._query({**self.params, **kwargs})

    @classmethod
    async def _query(cls, params: dict):
        async with AsyncClient() as client:
            return cls._parse(await client.get(cls.API, params=params, timeout=None))
