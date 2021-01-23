from typing import ClassVar, Type

from ..entity.root import ContentRoot
from ..enum import ElementPrefix
from .abstract import ItemType
from .abstract_item import Item
from ..entity.main import Content as Entity


class Content(Item[ContentRoot, Entity]):
    ID_TYPE: ClassVar[ElementPrefix] = ElementPrefix.CONTENT
    SEARCH_TYPE: ClassVar[ItemType] = ItemType.CONTENT
    CONSTRUCTOR: ClassVar[Type] = ContentRoot
