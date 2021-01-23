from dataclasses import dataclass

from ..common import ContentCommon
from .abstract_item import Item


@dataclass
class Content(ContentCommon, Item):
    ...
