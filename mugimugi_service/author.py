from typing import Iterable, Optional

from mugimugi_client_api import GetAuthorById, SearchAuthor
from mugimugi_client_api.enum import SortOrder
from mugimugi_client_api_entity import Author as Entity

from .abstract_item import Item


class Author(Item[Entity]):
    @classmethod
    def _get(self, ids: Iterable[int]) -> GetAuthorById:
        return GetAuthorById(ids)

    @classmethod
    def _search(
        self,
        title: Optional[str] = None,
        *,
        contributor: Optional[str] = None,
        sort_criterion: Optional[SearchAuthor.SortCriterion] = None,
        sort_order: Optional[SortOrder] = None,
    ) -> SearchAuthor:
        return SearchAuthor(
            title=title,
            contributor=contributor,
            sort_criterion=sort_criterion,
            sort_order=sort_order,
        )
