from typing import ClassVar, Type

from ..action import SearchItem
from ..bo.item.publisher import Item as Entity
from ..enum import ItemType
from .abstract_item import Item


class Publisher(Item[Entity]):
    ID_TYPE: ClassVar[ItemType] = ItemType.PUBLISHER
    SEARCH_TYPE: ClassVar[SearchItem.Type] = SearchItem.Type.PUBLISHER
    CONSTRUCTOR: ClassVar[Type] = Entity
