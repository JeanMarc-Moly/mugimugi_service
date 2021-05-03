from typing import Iterable

from ..action.get_item_by_id import GetImprintById
from ..entity.main import Imprint as Entity
from .abstract_item import Item


class Imprint(Item[Entity]):
    @classmethod
    def _get(self, ids: Iterable[int]) -> GetImprintById:
        return GetImprintById(ids)
