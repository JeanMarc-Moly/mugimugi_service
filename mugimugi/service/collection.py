from typing import Iterable, Optional

from ..action import GetCollectionById, SearchCollection
from ..entity.main import Collection as Entity
from ..enum import SortOrder
from .abstract_item import Item


class Collection(Item[Entity]):
    @classmethod
    def _get(self, ids: Iterable[int]) -> GetCollectionById:
        return GetCollectionById(ids)

    @classmethod
    def _search(
        self,
        title: Optional[str] = None,
        *,
        contributor: Optional[str] = None,
        sort_criterion: Optional[SearchCollection.SortCriterion] = None,
        sort_order: Optional[SortOrder] = None,
    ) -> SearchCollection:
        return SearchCollection(
            title=title,
            contributor=contributor,
            sort_criterion=sort_criterion,
            sort_order=sort_order,
        )
