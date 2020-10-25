from typing import ClassVar, Type

from ..action import SearchItem
from ..bo.item.character import Item as Entity
from ..enum import ItemType
from .abstract_item import Item


class Character(Item[Entity]):
    ID_TYPE: ClassVar[ItemType] = ItemType.CHARACTER
    SEARCH_TYPE: ClassVar[SearchItem.Type] = SearchItem.Type.CHARACTER
    CONSTRUCTOR: ClassVar[Type] = Entity
