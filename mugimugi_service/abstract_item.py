from abc import abstractmethod
from typing import AsyncGenerator, Generic, Optional

from mugimugi_client_api import SearchItem
from mugimugi_client_api.enum import SortOrder

from .abstract_getter import EI, Getter


class Item(Generic[EI], Getter[EI]):
    async def search(
        self,
        title: Optional[str] = None,
        *,
        contributor: Optional[str] = None,
        sort_criterion: Optional[SearchItem.SortCriterion] = None,
        sort_order: Optional[SortOrder] = None,
        limit: int = 0,
    ) -> AsyncGenerator[EI, None]:
        async with self._api.data as a:
            query = self._search(
                title,
                contributor=contributor,
                sort_criterion=sort_criterion,
                sort_order=sort_order,
            ).query_elements(a)
            async for element in query:
                yield element
                if not (limit := limit - 1):
                    return

    async def add(self, **kwargs) -> bool:
        raise Exception("Not Implemented")

    async def edit(self, **kwargs) -> bool:
        raise Exception("Not Implemented")

    async def delete(self, **kwargs) -> bool:
        raise Exception("Not Implemented")

    @classmethod
    @abstractmethod
    def _search(
        cls,
        title: Optional[str] = None,
        *,
        contributor: Optional[str] = None,
        sort_criterion: Optional[SearchItem.SortCriterion] = None,
        sort_order: Optional[SortOrder] = None,
    ) -> SearchItem:
        ...
