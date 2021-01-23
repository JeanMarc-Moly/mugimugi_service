from ..entity.main import Author as Entity
from typing import ClassVar, Type

from ..entity.root import AuthorRoot
from ..enum import ElementPrefix
from .abstract import ItemType
from .abstract_item import Item


class Author(Item[AuthorRoot, Entity]):
    ID_TYPE: ClassVar[ElementPrefix] = ElementPrefix.AUTHOR
    SEARCH_TYPE: ClassVar[ItemType] = ItemType.AUTHOR
    CONSTRUCTOR: ClassVar[Type] = AuthorRoot
