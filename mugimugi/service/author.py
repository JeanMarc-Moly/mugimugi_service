from typing import ClassVar, Type

from ..entity.item.author import AuthorRoot
from ..enum import ElementPrefix
from .abstract_item import Item
from .abstract import ItemType


class Author(Item[AuthorRoot]):
    ID_TYPE: ClassVar[ElementPrefix] = ElementPrefix.AUTHOR
    SEARCH_TYPE: ClassVar[ItemType] = ItemType.AUTHOR
    CONSTRUCTOR: ClassVar[Type] = AuthorRoot
