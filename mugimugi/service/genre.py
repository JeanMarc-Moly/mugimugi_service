from typing import ClassVar, Type

from ..entity.item.genre import GenreRoot
from ..enum import ElementPrefix
from .abstract import ItemType
from .abstract_item import Item


class Genre(Item[GenreRoot]):
    ID_TYPE: ClassVar[ElementPrefix] = ElementPrefix.GENRE
    SEARCH_TYPE: ClassVar[ItemType] = ItemType.GENRE
    CONSTRUCTOR: ClassVar[Type] = GenreRoot
