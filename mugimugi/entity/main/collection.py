from dataclasses import dataclass

from ..common import CollectionCommon
from .abstract_item import Item


@dataclass
class Collection(CollectionCommon, Item):
    ...
