from typing import Iterable, Optional

from ..action import GetAuthorById, SearchAuthor
from ..entity.main import Author as Entity
from ..enum.sort_order import SortOrder
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
