from dataclasses import dataclass
from typing import Callable

from mugimugi_client_api_entity import User as Entity
from mugimugi_client_api_entity.root import EmptyRoot


@dataclass
class User:
    _api: Callable
    # web: Callable

    async def get(self) -> Entity:
        return EmptyRoot.parse(await self._api({})).user
