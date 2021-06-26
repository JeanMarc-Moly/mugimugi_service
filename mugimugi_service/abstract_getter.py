from abc import abstractmethod
from dataclasses import dataclass
from typing import Generic, Iterable, Iterator, Optional, TypeVar

from mugimugi_client_api import GetItemById
from mugimugi_client_api_entity import Item
from multimethod import multimethod

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

    @classmethod
    @abstractmethod
    def _get(
        self, ids: Iterable[int]
    ) -> TypeVar("AbstractGetItemById", bound=GetItemById):
        ...
