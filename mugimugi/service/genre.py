from typing import ClassVar, Type

from ..entity.root import GenreRoot
from ..enum import ElementPrefix
from .abstract import ItemType
from .abstract_item import Item
from ..entity.main import Genre as Entity


class Genre(Item[GenreRoot, Entity]):
    ID_TYPE: ClassVar[ElementPrefix] = ElementPrefix.GENRE
    SEARCH_TYPE: ClassVar[ItemType] = ItemType.GENRE
    CONSTRUCTOR: ClassVar[Type] = GenreRoot
