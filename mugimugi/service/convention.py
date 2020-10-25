from datetime import date
from typing import AsyncIterator, ClassVar, Optional, Type

from ..action import SearchItem
from ..bo.item.convention import Item as Entity
from ..enum import ItemType, SortOrder
from .abstract_item import Item, parse_to_object


class Convention(Item[Entity]):
    ID_TYPE: ClassVar[ItemType] = ItemType.CONVENTION
    SEARCH_TYPE: ClassVar[SearchItem.Type] = SearchItem.Type.CONVENTION
    CONSTRUCTOR: ClassVar[Type] = Entity

    async def search(
        self,
        title: Optional[str] = None,
        *,
        date_: Optional[date] = None,
        contributor: Optional[str] = None,
        sort_criterion: Optional[SearchItem.SortCriterion] = None,
        sort_order: Optional[SortOrder] = None,
        limit: Optional[int] = None,
    ) -> AsyncIterator[Entity]:
        async for item in self.api.fetch_all_elements(
            SearchItem(
                title,
                self.SEARCH_TYPE,
                date_=date_,
                contributor=contributor,
                sort_criterion=sort_criterion,
                sort_order=sort_order,
            ),
            limit=limit,
        ):
            yield parse_to_object(item, self.CONSTRUCTOR)
