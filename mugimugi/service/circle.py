from typing import Iterable

from ..action.get_item_by_id import GetCircleById
from ..entity.main import Circle as Entity
from .abstract_item import Item


class Circle(Item[GetCircleById.Root, Entity]):
    @classmethod
    def _get(self, ids: Iterable[int]) -> GetCircleById:
        return GetCircleById(ids)
