from typing import ClassVar, Type

from ..action import SearchItem
from ..bo.item.genre import Item as Entity
from ..enum import ItemType
from .abstract_item import Item


class Genre(Item[Entity]):
    ID_TYPE: ClassVar[ItemType] = ItemType.GENRE
    SEARCH_TYPE: ClassVar[SearchItem.Type] = SearchItem.Type.GENRE
    CONSTRUCTOR: ClassVar[Type] = Entity
