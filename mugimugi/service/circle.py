from typing import ClassVar, Type

from ..action import SearchItem
from ..bo.item.circle import Item as Entity
from ..enum import ItemType
from .abstract_item import Item


class Circle(Item[Entity]):
    ID_TYPE: ClassVar[ItemType] = ItemType.CIRCLE
    SEARCH_TYPE: ClassVar[SearchItem.Type] = SearchItem.Type.CIRCLE
    CONSTRUCTOR: ClassVar[Type] = Entity
