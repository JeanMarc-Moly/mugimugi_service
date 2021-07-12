from abc import abstractmethod
from typing import AsyncIterator, Generic, Iterable, Optional, TypeVar

from mugimugi_client_api import GetItemById
from mugimugi_client_api_entity import Item
from multimethod import multimethod

from .abstract import AbstractService

EI = TypeVar("EI", bound=Item)


class Getter(Generic[EI], AbstractService):
    @multimethod
    async def get(self, id_: int) -> Optional[EI]:
        try:
            return await self.get((id_,)).__anext__()
        except StopAsyncIteration:
            return None

    @get.register
    async def _(self, ids: Iterable[int], fast=False) -> AsyncIterator[EI]:
        getter: GetItemById = self._get(ids)
        query = getter.query_elements_fast if fast else getter.query_elements_smart

        async with self._api.data as a:
            async for element in query(a):
                yield element

    @classmethod
    @abstractmethod
    def _get(cls, ids: Iterable[int]) -> GetItemById:
        ...
