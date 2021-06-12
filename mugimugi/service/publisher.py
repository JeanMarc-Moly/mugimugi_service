from typing import Iterable, Optional

from ..action import GetPublisherById, SearchPublisher
from ..entity.main import Publisher as Entity
from ..enum import SortOrder
from .abstract_item import Item


class Publisher(Item[Entity]):
    @classmethod
    def _get(self, ids: Iterable[int]) -> GetPublisherById:
        return GetPublisherById(ids)

    @classmethod
    def _search(
        self,
        title: Optional[str] = None,
        *,
        contributor: Optional[str] = None,
        sort_criterion: Optional[SearchPublisher.SortCriterion] = None,
        sort_order: Optional[SortOrder] = None,
    ) -> SearchPublisher:
        return SearchPublisher(
            title=title,
            contributor=contributor,
            sort_criterion=sort_criterion,
            sort_order=sort_order,
        )
