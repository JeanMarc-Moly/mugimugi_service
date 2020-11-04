from dataclasses import dataclass
from ..client import Client
from ..entity.root import EmptyRoot, User as UserEntity


@dataclass
class User:
    _api: Client
    # web: Callable

    async def get(self) -> UserEntity:
        return EmptyRoot.parse(await self._api.query({})).user
