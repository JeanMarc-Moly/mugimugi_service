from typing import ClassVar, Type

from ..entity.root import CollectionRoot
from ..enum import ElementPrefix
from .abstract import ItemType
from .abstract_item import Item

from ..entity.main import Collection as Entity


class Collection(Item[CollectionRoot, Entity]):
    ID_TYPE: ClassVar[ElementPrefix] = ElementPrefix.COLLECTION
    SEARCH_TYPE: ClassVar[ItemType] = ItemType.COLLECTION
    CONSTRUCTOR: ClassVar[Type] = CollectionRoot
