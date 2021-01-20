from typing import ClassVar, Type

from ..entity.item.character import CharacterRoot
from ..enum import ElementPrefix
from .abstract import ItemType
from .abstract_item import Item


class Character(Item[CharacterRoot]):
    ID_TYPE: ClassVar[ElementPrefix] = ElementPrefix.CHARACTER
    SEARCH_TYPE: ClassVar[ItemType] = ItemType.CHARACTER
    CONSTRUCTOR: ClassVar[Type] = CharacterRoot
