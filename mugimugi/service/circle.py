from typing import ClassVar, Type

from ..entity.item.circle import CircleRoot
from ..enum import ElementPrefix
from .abstract_item import Item
from .abstract import ItemType


class Circle(Item[CircleRoot]):
    ID_TYPE: ClassVar[ElementPrefix] = ElementPrefix.CIRCLE
    SEARCH_TYPE: ClassVar[ItemType] = ItemType.CIRCLE
    CONSTRUCTOR: ClassVar[Type] = CircleRoot
