from contextlib import suppress
from datetime import date
from typing import AsyncIterator, Coroutine, Iterable, Iterator, Optional

from ..action import SearchItem
from ..action.get_item_by_id import GetConventionById
from ..entity.main import Convention as Entity
from ..enum import SortOrder
from .abstract_item import Item


class Convention(Item[GetConventionById.Root, Entity]):
    @classmethod
    def _get(self, ids: Iterable[int]) -> GetConventionById.Root:
        return GetConventionById(ids)

    async def search(
        self,
        title: Optional[str] = None,
        *,
        date_: Optional[date] = None,
        contributor: Optional[str] = None,
        sort_criterion: Optional[SearchItem.SortCriterion] = None,
        sort_order: Optional[SortOrder] = None,
        limit: Optional[int] = 0,
    ) -> AsyncIterator[GetConventionById.Root]:  # TODO change when defined for search
        with suppress(StopIteration):
            parse = self.CONSTRUCTOR.parse
            pages = self.search_pages(
                title, date_, contributor, sort_criterion, sort_order
            )
            page = None
            while page := pages.send(page):
                page = parse(await page)
                for element in page.elements:
                    yield element
                    if not (limit := limit - 1):
                        return

    def search_pages(
        self,
        title: Optional[str] = None,
        date_: Optional[date] = None,
        contributor: Optional[str] = None,
        sort_criterion: Optional[SearchItem.SortCriterion] = None,
        sort_order: Optional[SortOrder] = None,
    ) -> Iterator[Coroutine]:
        action = iter(
            SearchItem(
                self.SEARCH_TYPE,
                title,
                date_=date_,
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
