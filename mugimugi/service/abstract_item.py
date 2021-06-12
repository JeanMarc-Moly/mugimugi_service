from abc import abstractmethod
from dataclasses import dataclass
from typing import Generic, Iterator, Optional, TypeVar

from ..action import SearchItem
from ..enum import SortOrder
from .abstract import AbstractService
from .abstract_getter import EI, Getter


@dataclass
class Item(Generic[EI], AbstractService, Getter[EI]):
    async def search(
        self,
        title: Optional[str] = None,
        *,
        contributor: Optional[str] = None,
        sort_criterion: Optional[SearchItem.SortCriterion] = None,
        sort_order: Optional[SortOrder] = None,
        limit: Optional[int] = 0,
    ) -> Iterator[EI]:
        query = self._search(
            title,
            contributor=contributor,
            sort_criterion=sort_criterion,
            sort_order=sort_order,
        ).query_elements
        async for element in query(self._api):
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
        self,
        title: Optional[str] = None,
        *,
        contributor: Optional[str] = None,
        sort_criterion: Optional[SearchItem.SortCriterion] = None,
        sort_order: Optional[SortOrder] = None,
    ) -> TypeVar("AbstractSearchItem", bound=SearchItem):
        ...
