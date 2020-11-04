from typing import ClassVar, Type

from ..entity.item.content import ContentRoot
from ..enum import ElementPrefix
from .abstract_item import Item
from .abstract import ItemType


class Content(Item[ContentRoot]):
    ID_TYPE: ClassVar[ElementPrefix] = ElementPrefix.CONTENT
    SEARCH_TYPE: ClassVar[ItemType] = ItemType.CONTENT
    CONSTRUCTOR: ClassVar[Type] = ContentRoot
