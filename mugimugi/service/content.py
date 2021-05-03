from typing import Iterable

from ..action.get_item_by_id import GetContentById
from ..entity.main import Content as Entity
from .abstract_item import Item


class Content(Item[GetContentById.Root, Entity]):
    @classmethod
    def _get(self, ids: Iterable[int]) -> GetContentById:
        return GetContentById(ids)
