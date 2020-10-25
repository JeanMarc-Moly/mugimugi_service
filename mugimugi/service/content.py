from typing import ClassVar, Type

from ..action import SearchItem
from ..bo.item.contents import Item as Entity
from ..enum import ItemType
from .abstract_item import Item


class Content(Item[Entity]):
    ID_TYPE: ClassVar[ItemType] = ItemType.CONTENT
    SEARCH_TYPE: ClassVar[SearchItem.Type] = SearchItem.Type.CONTENT
    CONSTRUCTOR: ClassVar[Type] = Entity
