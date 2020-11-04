from datetime import date
from typing import AsyncIterator, ClassVar, Optional, Type

from ..action import SearchItem
from ..entity.item.convention import ConventionRoot
from ..enum import ElementPrefix, SortOrder, ItemType
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
        limit: Optional[int] = None,
    ) -> AsyncIterator[ConventionRoot]:
        async for item in self.fetch_all_elements(
            SearchItem(
                self.SEARCH_TYPE,
                title,
                date_=date_,
                contributor=contributor,
                sort_criterion=sort_criterion,
                sort_order=sort_order,
            ),
            limit=limit,
        ):
            yield item
