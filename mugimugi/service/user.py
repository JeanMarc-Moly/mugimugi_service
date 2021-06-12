from dataclasses import dataclass
from typing import Callable

from ..entity.main import User as Entity
from ..entity.root import EmptyRoot


@dataclass
class User:
    _api: Callable
    # web: Callable

    async def get(self) -> Entity:
        return EmptyRoot.parse(await self._api({})).user
