from typing import ClassVar, Type

from ..entity.main import Imprint as Entity
from ..entity.root import ImprintRoot
from ..enum import ElementPrefix
from .abstract import ItemType
from .abstract_item import Item


class Imprint(Item[ImprintRoot, Entity]):
    ID_TYPE: ClassVar[ElementPrefix] = ElementPrefix.IMPRINT
    SEARCH_TYPE: ClassVar[ItemType] = ItemType.IMPRINT
    CONSTRUCTOR: ClassVar[Type] = ImprintRoot
