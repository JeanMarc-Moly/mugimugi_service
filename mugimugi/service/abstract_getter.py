from asyncio import as_completed, run, wait
from dataclasses import dataclass
from typing import Coroutine, Generic, Iterable, Iterator, Optional, TypeVar, Union

from multimethod import multimethod

from ..action import GetItemById
from ..entity.main import Item

EI = TypeVar("EI", bound=Item)


@dataclass
class Getter(Generic[EI]):
    @multimethod
    async def get(self, ids: Iterable[int]) -> Iterator[EI]:
        parse = self.CONSTRUCTOR.parse
        for page in self.get_pages(ids):
            for element in parse(await page).elements:
                yield element

    @multimethod
    async def get(self, ids: Iterable[str]) -> Iterator[EI]:
        prefix = self.ID_TYPE.value
        async for item in self.get({int(i.removeprefix(prefix)) for i in ids}):
            yield item

    @multimethod
    async def get(self, id_: int) -> Optional[EI]:
        try:
            return await self.get((id_,)).__anext__()
        except StopAsyncIteration:
            return None

    @multimethod
    async def get(self, id_: str) -> Optional[EI]:
        return await self.get(int(id_.removeprefix(self.ID_TYPE.value)))

    @multimethod
    def get_(self, ids: Iterable[Union[str, int]]) -> Iterator[EI]:
        parse = self.CONSTRUCTOR.parse
        for page in self.get_pages(ids):
            for element in parse(run(page)).elements:
                yield element

    @multimethod
    def get_(self, id_: Union[str, int]) -> Optional[EI]:
        return next(self.get_([id_]))

    async def get_all(self, ids: Iterable[int]) -> Iterator[EI]:
        parse = self.CONSTRUCTOR.parse
        for page in as_completed(list(self.get_pages(ids))):
            for element in parse(await page).elements:
                yield element

    def get_all_(self, ids: Iterable[Union[str, int]]) -> Iterator[EI]:
        parse = self.CONSTRUCTOR.parse
        # TODO: find a way to use `as_completed` or equivalent for better perf
        pages, _ = run(wait(list(self.get_pages(ids))))
        for page in pages:
            for element in parse(page.result()).elements:
                yield element

    def get_pages(self, ids) -> Iterator[Coroutine]:
        type_ = self.ID_TYPE
        query = self._api.query
        for action in GetItemById((type_, id_) for id_ in ids):
            yield query(action)
