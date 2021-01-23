from dataclasses import dataclass
from typing import ClassVar, Generic, Iterator, Optional, Type, TypeVar

from ..entity.root import AbstractRoot

from ..action import AbstractAction, AbstractPaginatedAction
from ..client import Client
from ..enum import ElementPrefix, ItemType

E = TypeVar("E", bound=AbstractRoot)


@dataclass
class AbstractService(Generic[E]):
    ID_TYPE: ClassVar[ElementPrefix]
    SEARCH_TYPE: ClassVar[ItemType]
    CONSTRUCTOR: ClassVar[Type[E]]
    # MAX_PER_PAGE: ClassVar[int] = REQUEST_GET_ID_MAX_COUNT

    _api: Client
    # web: Callable

    async def fetch_all(self, action: AbstractPaginatedAction):
        max_ = self.MAX_PER_PAGE
        parser = self.CONSTRUCTOR.parse
        action.page = 1
        while len(elements := parser(await self._api.query(action)).elements) <= max_:
            yield elements
            action.page += 1

    async def fetch_all_elements(
        self, action: AbstractPaginatedAction, limit: Optional[int] = None,
    ) -> Iterator[E]:
        async for page in self.fetch_all(action):
            for elements in page:
                yield elements
                if limit and not (limit := limit - 1):
                    return

    async def fetch_elements(self, action: AbstractAction,) -> Iterator[E]:
        for element in self.CONSTRUCTOR.parse.parse(
            await self._api.query(action)
        ).elements:
            yield element
