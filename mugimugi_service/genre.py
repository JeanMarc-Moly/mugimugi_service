from typing import Iterable, Optional

from mugimugi_client_api import GetGenreById, SearchGenre
from mugimugi_client_api.enum import SortOrder
from mugimugi_client_api_entity import Genre as Entity

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
