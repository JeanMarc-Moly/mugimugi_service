from typing import ClassVar, Type

from ..entity.item.circle import CircleRoot
from ..enum import ElementPrefix
from .abstract import ItemType
from .abstract_item import Item


class Circle(Item[CircleRoot]):
    ID_TYPE: ClassVar[ElementPrefix] = ElementPrefix.CIRCLE
    SEARCH_TYPE: ClassVar[ItemType] = ItemType.CIRCLE
    CONSTRUCTOR: ClassVar[Type] = CircleRoot
