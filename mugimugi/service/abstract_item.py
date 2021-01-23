from asyncio import run
from contextlib import suppress
from dataclasses import dataclass
from typing import Coroutine, Generic, Iterator, Optional

from ..action import SearchItem
from ..enum import SortOrder
from .abstract import AbstractService, E
from .abstract_getter import EI, Getter


@dataclass
class Item(Generic[E, EI], AbstractService[E], Getter[EI]):
    async def search(
        self,
        title: Optional[str] = None,
        *,
        contributor: Optional[str] = None,
        sort_criterion: Optional[SearchItem.SortCriterion] = None,
        sort_order: Optional[SortOrder] = None,
        limit: Optional[int] = 0,
    ) -> Iterator[EI]:
        with suppress(StopIteration):
            parse = self.CONSTRUCTOR.parse
            pages = self.search_pages(title, contributor, sort_criterion, sort_order)
            page = None
            while page := pages.send(page):
                page = parse(await page)
                for element in page.elements:
                    yield element
                    if not (limit := limit - 1):
                        return

    def search_(
        self,
        title: Optional[str] = None,
        *,
        contributor: Optional[str] = None,
        sort_criterion: Optional[SearchItem.SortCriterion] = None,
        sort_order: Optional[SortOrder] = None,
        limit: Optional[int] = 0,
    ) -> Iterator[EI]:
        with suppress(StopIteration):
            parse = self.CONSTRUCTOR.parse
            pages = self.search_pages(title, contributor, sort_criterion, sort_order)
            page = None
            while page := pages.send(page):
                page = parse(run(page))
                for element in page.elements:
                    yield element
                    if not (limit := limit - 1):
                        return

    def search_pages(
        self,
        title: Optional[str] = None,
        contributor: Optional[str] = None,
        sort_criterion: Optional[SearchItem.SortCriterion] = None,
        sort_order: Optional[SortOrder] = None,
    ) -> Iterator[Coroutine]:
        action = iter(
            SearchItem(
                self.SEARCH_TYPE,
                title,
                contributor=contributor,
                sort_criterion=sort_criterion,
                sort_order=sort_order,
            )
        )
        query = self._api.query
        response = None
        with suppress(StopIteration):
            while paginated_action := action.send(response):
                response = yield query(paginated_action)

    async def add(self, **kwargs) -> bool:
        raise Exception("Not Implemented")

    async def edit(self, **kwargs) -> bool:
        raise Exception("Not Implemented")

    async def delete(self, **kwargs) -> bool:
        raise Exception("Not Implemented")
