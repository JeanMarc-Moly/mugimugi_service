from typing import ClassVar, Type

from ..entity.root import CharacterRoot
from ..enum import ElementPrefix
from .abstract import ItemType
from .abstract_item import Item
from ..entity.main import Character as Entity


class Character(Item[CharacterRoot, Entity]):
    ID_TYPE: ClassVar[ElementPrefix] = ElementPrefix.CHARACTER
    SEARCH_TYPE: ClassVar[ItemType] = ItemType.CHARACTER
    CONSTRUCTOR: ClassVar[Type] = CharacterRoot
