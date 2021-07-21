from typing import Iterable, Optional

from mugimugi_client_api import GetCharacterById, SearchCharacter
from mugimugi_client_api.enum import SortOrder
from mugimugi_client_api_entity import Character as Entity

from .abstract_item import Item


class Character(Item[Entity]):
    @classmethod
    def _get(cls, ids: Iterable[int]) -> GetCharacterById:
        return GetCharacterById(ids)

    @classmethod
    def _search(
        cls,
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
