from dataclasses import dataclass
from typing import (
    AsyncIterator,
    Awaitable,
    ClassVar,
    Generic,
    Iterable,
    Optional,
    Type,
    TypeVar,
)

from multimethod import multimethod

from ..action import GetItemById, SearchItem
from ..client import Client
from ..enum import ItemType, SortOrder
from ..util.xml import parse_to_object

E = TypeVar("E")


@dataclass
class Item(Generic[E]):
    ID_TYPE: ClassVar[ItemType]
    SEARCH_TYPE: ClassVar[SearchItem.Type]
    CONSTRUCTOR: ClassVar[Type]

    api: Client
    # web: Callable

    @multimethod
    async def get(self, ids: Iterable[int]) -> AsyncIterator[E]:
        async for item in self.api.fetch_elements(
            GetItemById((self.ID_TYPE, id_) for id_ in ids)
        ):
            yield parse_to_object(item, self.CONSTRUCTOR)

    @multimethod
    async def get(self, ids: Iterable[str]) -> AsyncIterator[E]:
        async for item in self.get(
            {int(i.removeprefix(self.ID_TYPE.value)) for i in ids}
        ):
            yield item

    @multimethod
    async def get(self, id_: int) -> Awaitable[E]:
        return await self.get((id_,)).__anext__()

    @multimethod
    async def get(self, id_: str) -> Awaitable[E]:
        return await self.get(int(id_.removeprefix(self.ID_TYPE.value)))

    async def search(
        self,
        title: Optional[str] = None,
        *,
        contributor: Optional[str] = None,
        sort_criterion: Optional[SearchItem.SortCriterion] = None,
        sort_order: Optional[SortOrder] = None,
        limit: Optional[int] = None,
    ) -> AsyncIterator[E]:
        async for item in self.api.fetch_all_elements(
            SearchItem(
                title,
                self.SEARCH_TYPE,
                contributor=contributor,
                sort_criterion=sort_criterion,
                sort_order=sort_order,
            ),
            limit=limit,
        ):
            yield parse_to_object(item, self.CONSTRUCTOR)

    async def add(self, **kwargs) -> E:
        raise Exception("Not Implemented")

    async def edit(self, **kwargs) -> E:
        raise Exception("Not Implemented")

    async def delete(self, **kwargs) -> E:
        raise Exception("Not Implemented")
