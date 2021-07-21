from typing import Iterable, Optional

from mugimugi_client_api import GetCollectionById, SearchCollection
from mugimugi_client_api.enum import SortOrder
from mugimugi_client_api_entity import Collection as Entity

from .abstract_item import Item


class Collection(Item[Entity]):
    @classmethod
    def _get(cls, ids: Iterable[int]) -> GetCollectionById:
        return GetCollectionById(ids)

    @classmethod
    def _search(
        cls,
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
