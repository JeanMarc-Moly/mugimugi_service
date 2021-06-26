from typing import Iterable, Optional

from mugimugi_client_api import GetCircleById, SearchCircle
from mugimugi_client_api.enum import SortOrder
from mugimugi_client_api_entity import Circle as Entity

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
