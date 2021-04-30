from typing import Iterable

from ..action.get_item_by_id import GetImprintById
from ..entity.main import Imprint as Entity
from .abstract_item import Item


class Imprint(Item[GetImprintById.Root, Entity]):
    @classmethod
    def _get(self, ids: Iterable[int]) -> GetImprintById.Root:
        return GetImprintById(ids)
