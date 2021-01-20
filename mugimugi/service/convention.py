from contextlib import suppress
from datetime import date
from typing import AsyncIterator, ClassVar, Coroutine, Iterator, Optional, Type

from ..action import SearchItem
from ..entity.item.convention import ConventionRoot
from ..enum import ElementPrefix, ItemType, SortOrder
from .abstract_item import Item


class Convention(Item[ConventionRoot]):
    ID_TYPE: ClassVar[ElementPrefix] = ElementPrefix.CONVENTION
    SEARCH_TYPE: ClassVar[ItemType] = ItemType.CONVENTION
    CONSTRUCTOR: ClassVar[Type] = ConventionRoot

    async def search(
        self,
        title: Optional[str] = None,
        *,
        date_: Optional[date] = None,
        contributor: Optional[str] = None,
        sort_criterion: Optional[SearchItem.SortCriterion] = None,
        sort_order: Optional[SortOrder] = None,
        limit: Optional[int] = 0,
    ) -> AsyncIterator[ConventionRoot]:
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
