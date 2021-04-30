from typing import Iterable

from ..action.get_item_by_id import GetGenreById
from ..entity.main import Genre as Entity
from .abstract_item import Item


class Genre(Item[GetGenreById.Root, Entity]):
    @classmethod
    def _get(self, ids: Iterable[int]) -> GetGenreById.Root:
        return GetGenreById(ids)
