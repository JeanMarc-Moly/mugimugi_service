from dataclasses import dataclass

from ..client import Client
from ..entity.main import User as Entity
from ..entity.root import EmptyRoot


@dataclass
class User:
    _api: Client
    # web: Callable

    async def get(self) -> Entity:
        return EmptyRoot.parse(await self._api.query({})).user
