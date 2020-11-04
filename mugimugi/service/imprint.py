from typing import ClassVar, Type

from ..entity.item.imprint import ImprintRoot
from ..enum import ElementPrefix
from .abstract_item import Item
from .abstract import ItemType


class Imprint(Item[ImprintRoot]):
    ID_TYPE: ClassVar[ElementPrefix] = ElementPrefix.IMPRINT
    SEARCH_TYPE: ClassVar[ItemType] = ItemType.IMPRINT
    CONSTRUCTOR: ClassVar[Type] = ImprintRoot
