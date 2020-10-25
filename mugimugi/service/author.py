from typing import ClassVar, Type

from ..action import SearchItem
from ..bo.item.author import Item as Entity
from ..enum import ItemType
from .abstract_item import Item


class Author(Item[Entity]):
    ID_TYPE: ClassVar[ItemType] = ItemType.AUTHOR
    SEARCH_TYPE: ClassVar[SearchItem.Type] = SearchItem.Type.AUTHOR
    CONSTRUCTOR: ClassVar[Type] = Entity
