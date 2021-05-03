from typing import Iterable

from ..action.get_item_by_id import GetCollectionById
from ..entity.main import Collection as Entity
from .abstract_item import Item


class Collection(Item[Entity]):
    @classmethod
    def _get(self, ids: Iterable[int]) -> GetCollectionById:
        return GetCollectionById(ids)
