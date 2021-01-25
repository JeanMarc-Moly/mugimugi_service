from typing import ClassVar, Type

from ..entity.main import Parody as Entity
from ..entity.root import ParodyRoot
from ..enum import ElementPrefix
from .abstract import ItemType
from .abstract_item import Item


class Parody(Item[ParodyRoot, Entity]):
    ID_TYPE: ClassVar[ElementPrefix] = ElementPrefix.PARODY
    SEARCH_TYPE: ClassVar[ItemType] = ItemType.PARODY
    CONSTRUCTOR: ClassVar[Type] = ParodyRoot
