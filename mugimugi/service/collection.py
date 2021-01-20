from typing import ClassVar, Type

from ..entity.item.collection import CollectionRoot
from ..enum import ElementPrefix
from .abstract import ItemType
from .abstract_item import Item


class Collection(Item[CollectionRoot]):
    ID_TYPE: ClassVar[ElementPrefix] = ElementPrefix.COLLECTION
    SEARCH_TYPE: ClassVar[ItemType] = ItemType.COLLECTION
    CONSTRUCTOR: ClassVar[Type] = CollectionRoot
