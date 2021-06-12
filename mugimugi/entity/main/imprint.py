from dataclasses import dataclass

from ..common import ImprintCommon
from .abstract_item import Item


@dataclass
class Imprint(ImprintCommon, Item):
    ...
