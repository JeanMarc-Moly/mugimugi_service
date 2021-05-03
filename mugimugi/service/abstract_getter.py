from abc import abstractmethod
from dataclasses import dataclass
from typing import Generic, Iterable, Iterator, Optional, TypeVar

from multimethod import multimethod

from ..entity.main import Item

EI = TypeVar("EI", bound=Item)


@dataclass
class Getter(Generic[EI]):
    @multimethod
    async def get(self, ids: Iterable[int]) -> Iterator[EI]:
        async for element in self._get(ids).query_elements_smart(self._api):
            yield element

    @multimethod
    async def get(self, id_: int) -> Optional[EI]:
        try:
            return await self.get((id_,)).__anext__()
        except StopAsyncIteration:
            return None

    async def get_all(self, ids: Iterable[int]) -> Iterator[EI]:
        async for element in self._get(ids).query_elements_fast(self._api):
            yield element

    @classmethod
    @abstractmethod
    def _get(
        self, ids: Iterable[int]
    ) -> TypeVar("AbstractGetItemById", bound=GetItemById):
        ...
