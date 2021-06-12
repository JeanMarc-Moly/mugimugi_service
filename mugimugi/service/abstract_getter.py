from abc import abstractmethod
from dataclasses import dataclass
from typing import Generic, Iterable, Iterator, Optional, TypeVar

from multimethod import multimethod

from ..action.get_item_by_id.abstract import GetItemById
from ..entity.main import Item

EI = TypeVar("EI", bound=Item)


@dataclass
class Getter(Generic[EI]):
    @multimethod
    async def get(self, id_: int) -> Optional[EI]:
        try:
            return await self.get((id_,)).__anext__()
        except StopAsyncIteration:
            return None

    @multimethod
    async def get(self, ids: Iterable[int], fast=False) -> Iterator[EI]:
        query = self._get(ids)
        query = query.query_elements_fast if fast else query.query_elements_smart
        async for element in query(self._api):
            yield element

    # @multimethod
    # def get_(self, ids: Iterable[int]) -> Iterator[EI]:
    #     elements = self.get(ids)
    #     while e := run(elements.__anext__()):
    #         yield e

    # @multimethod
    # def get_(self, id_: int) -> Optional[EI]:
    #     return run(self.get(id_))

    # def get_all_(self, ids: Iterable[int]) -> Iterator[EI]:
    #     elements = self.get_all(ids)
    #     while e := run(elements.__anext__()):
    #         yield e

    @classmethod
    @abstractmethod
    def _get(
        self, ids: Iterable[int]
    ) -> TypeVar("AbstractGetItemById", bound=GetItemById):
        ...
