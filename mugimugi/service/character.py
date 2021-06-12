from typing import Iterable, Optional

from ..action import GetCharacterById, SearchCharacter
from ..entity.main import Character as Entity
from ..enum import SortOrder
from .abstract_item import Item


class Character(Item[Entity]):
    @classmethod
    def _get(self, ids: Iterable[int]) -> GetCharacterById:
        return GetCharacterById(ids)

    @classmethod
    def _search(
        self,
        title: Optional[str] = None,
        *,
        contributor: Optional[str] = None,
        sort_criterion: Optional[SearchCharacter.SortCriterion] = None,
        sort_order: Optional[SortOrder] = None,
    ) -> SearchCharacter:
        return SearchCharacter(
            title=title,
            contributor=contributor,
            sort_criterion=sort_criterion,
            sort_order=sort_order,
        )
