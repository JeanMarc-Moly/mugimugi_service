from typing import ClassVar, Type

from ..entity.item.parody import ParodyRoot
from ..enum import ElementPrefix
from .abstract import ItemType
from .abstract_item import Item


class Parody(Item[ParodyRoot]):
    ID_TYPE: ClassVar[ElementPrefix] = ElementPrefix.PARODY
    SEARCH_TYPE: ClassVar[ItemType] = ItemType.PARODY
    CONSTRUCTOR: ClassVar[Type] = ParodyRoot
