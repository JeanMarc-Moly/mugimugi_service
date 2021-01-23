from typing import ClassVar, Type

from ..entity.root import PublisherRoot
from ..enum import ElementPrefix
from .abstract import ItemType
from .abstract_item import Item
from ..entity.main import Publisher as Entity


class Publisher(Item[PublisherRoot, Entity]):
    ID_TYPE: ClassVar[ElementPrefix] = ElementPrefix.PUBLISHER
    SEARCH_TYPE: ClassVar[ItemType] = ItemType.PUBLISHER
    CONSTRUCTOR: ClassVar[Type] = PublisherRoot
