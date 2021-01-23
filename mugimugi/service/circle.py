from typing import ClassVar, Type

from ..entity.root import CircleRoot
from ..enum import ElementPrefix
from .abstract import ItemType
from .abstract_item import Item
from ..entity.main import Circle as Entity


class Circle(Item[CircleRoot, Entity]):
    ID_TYPE: ClassVar[ElementPrefix] = ElementPrefix.CIRCLE
    SEARCH_TYPE: ClassVar[ItemType] = ItemType.CIRCLE
    CONSTRUCTOR: ClassVar[Type] = CircleRoot
