from typing import ClassVar, Type

from ..action import SearchItem
from ..bo.item.collections import Item as Entity
from ..enum import ItemType
from .abstract_item import Item


class Collection(Item[Entity]):
    ID_TYPE: ClassVar[ItemType] = ItemType.COLLECTION
    SEARCH_TYPE: ClassVar[SearchItem.Type] = SearchItem.Type.COLLECTION
    CONSTRUCTOR: ClassVar[Type] = Entity
