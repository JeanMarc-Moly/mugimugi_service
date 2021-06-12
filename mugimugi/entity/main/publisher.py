from dataclasses import dataclass

from ..common import PublisherCommon
from .abstract_item import Item


@dataclass
class Publisher(PublisherCommon, Item):
    ...
