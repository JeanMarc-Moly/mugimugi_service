from typing import Iterable, Optional

from ..action import GetGenreById, SearchGenre
from ..entity.main import Genre as Entity
from ..enum import SortOrder
from .abstract_item import Item


class Genre(Item[Entity]):
    @classmethod
    def _get(self, ids: Iterable[int]) -> GetGenreById:
        return GetGenreById(ids)

    @classmethod
    def _search(
        self,
        title: Optional[str] = None,
        *,
        contributor: Optional[str] = None,
        sort_criterion: Optional[SearchGenre.SortCriterion] = None,
        sort_order: Optional[SortOrder] = None,
    ) -> SearchGenre:
        return SearchGenre(
            title=title,
            contributor=contributor,
            sort_criterion=sort_criterion,
            sort_order=sort_order,
        )
