from typing import Iterable, Optional

from mugimugi_client_api import GetContentById, SearchContent
from mugimugi_client_api.enum import SortOrder
from mugimugi_client_api_entity import Content as Entity

from .abstract_item import Item


class Content(Item[Entity]):
    @classmethod
    def _get(self, ids: Iterable[int]) -> GetContentById:
        return GetContentById(ids)

    @classmethod
    def _search(
        self,
        title: Optional[str] = None,
        *,
        contributor: Optional[str] = None,
        sort_criterion: Optional[SearchContent.SortCriterion] = None,
        sort_order: Optional[SortOrder] = None,
    ) -> SearchContent:
        return SearchContent(
            title=title,
            contributor=contributor,
            sort_criterion=sort_criterion,
            sort_order=sort_order,
        )
