from mugimugi_client_api_entity import User as Entity
from mugimugi_client_api_entity.root import EmptyRoot

from .abstract import AbstractService


class User(AbstractService):
    async def get(self) -> Entity:
        async with self._api.data as c:
            return EmptyRoot.parse((await c.get("")).text)
