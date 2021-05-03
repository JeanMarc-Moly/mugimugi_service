from typing import Iterable

from ..action.get_item_by_id import GetCharacterById
from ..entity.main import Character as Entity
from .abstract_item import Item


class Character(Item[Entity]):
    @classmethod
    def _get(self, ids: Iterable[int]) -> GetCharacterById:
        return GetCharacterById(ids)
