from typing import Iterable, Optional

from ..action import GetCircleById, SearchCircle
from ..entity.main import Circle as Entity
from ..enum import SortOrder
from .abstract_item import Item


class Circle(Item[Entity]):
    @classmethod
    def _get(self, ids: Iterable[int]) -> GetCircleById:
        return GetCircleById(ids)

    @classmethod
    def _search(
        self,
        title: Optional[str] = None,
        *,
        contributor: Optional[str] = None,
        sort_criterion: Optional[SearchCircle.SortCriterion] = None,
        sort_order: Optional[SortOrder] = None,
    ) -> SearchCircle:
        return SearchCircle(
            title=title,
            contributor=contributor,
            sort_criterion=sort_criterion,
            sort_order=sort_order,
        )
