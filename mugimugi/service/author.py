from typing import Iterable

from ..action.get_item_by_id import GetAuthorById
from ..entity.main import Author as Entity
from .abstract_item import Item


class Author(Item[GetAuthorById.Root, Entity]):
    @classmethod
    def _get(self, ids: Iterable[int]) -> GetAuthorById:
        return GetAuthorById(ids)
