from typing import ClassVar, Type

from ..action import SearchItem
from ..bo.item.parody import Item as Entity
from ..enum import ItemType
from .abstract_item import Item


class Parody(Item[Entity]):
    ID_TYPE: ClassVar[ItemType] = ItemType.PARODY
    SEARCH_TYPE: ClassVar[SearchItem.Type] = SearchItem.Type.PARODY
    CONSTRUCTOR: ClassVar[Type] = Entity
