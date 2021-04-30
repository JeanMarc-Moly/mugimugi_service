from dataclasses import dataclass
from typing import Callable, ClassVar, Generic, Iterator, Optional, Type, TypeVar

from ..action import AbstractAction, AbstractPaginatedAction
from ..entity.root import AbstractRoot
from ..enum import ElementPrefix, ItemType

E = TypeVar("E", bound=AbstractRoot)


@dataclass
class AbstractService(Generic[E]):
    ID_TYPE: ClassVar[ElementPrefix]
    SEARCH_TYPE: ClassVar[ItemType]
    CONSTRUCTOR: ClassVar[Type[E]]
    # MAX_PER_PAGE: ClassVar[int] = REQUEST_GET_ID_MAX_COUNT

    _api: Callable
    # web: Callable

    async def fetch_all(self, action: AbstractPaginatedAction):
        max_ = self.MAX_PER_PAGE
        action.page = 1
        while len(elements := self.query(action)) <= max_:
            yield elements
            action.page += 1

    async def fetch_all_elements(
        self,
        action: AbstractPaginatedAction,
        limit: Optional[int] = None,
    ) -> Iterator[E]:
        async for page in self.fetch_all(action):
            for elements in page:
                yield elements
                if limit and not (limit := limit - 1):
                    return

    async def fetch_elements(self, action: AbstractAction) -> Iterator[E]:
        for element in self.query(action):
            yield element
