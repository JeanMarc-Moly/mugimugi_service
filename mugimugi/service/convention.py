from datetime import date
from typing import Iterable, Iterator, Optional

from ..action import GetConventionById, SearchConvention, SearchItem
from ..entity.main import Convention as Entity
from ..enum import SortOrder
from .abstract_item import Item


class Convention(Item[Entity]):
    @classmethod
    def _get(self, ids: Iterable[int]) -> GetConventionById:
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
    ) -> Iterator[Entity]:
        query = SearchConvention(
            title=title,
            date_=date_,
            contributor=contributor,
            sort_criterion=sort_criterion,
            sort_order=sort_order,
        ).query_elements
        async for element in query(self._api):
            yield element
            if not (limit := limit - 1):
                return
