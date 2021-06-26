from typing import Iterable, Optional

from mugimugi_client_api import GetParodyById, SearchParody
from mugimugi_client_api.enum import SortOrder
from mugimugi_client_api_entity import Parody as Entity

from .abstract_item import Item


class Parody(Item[Entity]):
    @classmethod
    def _get(self, ids: Iterable[int]) -> GetParodyById:
        return GetParodyById(ids)

    @classmethod
    def _search(
        self,
        title: Optional[str] = None,
        *,
        contributor: Optional[str] = None,
        sort_criterion: Optional[SearchParody.SortCriterion] = None,
        sort_order: Optional[SortOrder] = None,
    ) -> SearchParody:
        return SearchParody(
            title=title,
            contributor=contributor,
            sort_criterion=sort_criterion,
            sort_order=sort_order,
        )
