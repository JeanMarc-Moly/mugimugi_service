from typing import Iterable, Optional

from ..action import GetContentById, SearchContent
from ..entity.main import Content as Entity
from ..enum import SortOrder
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
