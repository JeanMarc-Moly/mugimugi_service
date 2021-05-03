from typing import Iterable

from ..action.get_item_by_id import GetParodyById
from ..entity.main import Parody as Entity
from .abstract_item import Item


class Parody(Item[GetParodyById.Root, Entity]):
    @classmethod
    def _get(self, ids: Iterable[int]) -> GetParodyById:
        return GetParodyById(ids)
