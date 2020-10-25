from typing import ClassVar, Type

from ..action import SearchItem
from ..bo.item.imprint import Item as Entity
from ..enum import ItemType
from .abstract_item import Item


class Imprint(Item[Entity]):
    ID_TYPE: ClassVar[ItemType] = ItemType.IMPRINT
    SEARCH_TYPE: ClassVar[SearchItem.Type] = SearchItem.Type.IMPRINT
    CONSTRUCTOR: ClassVar[Type] = Entity
