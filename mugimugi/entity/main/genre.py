from dataclasses import dataclass

from ..common import GenreCommon
from .abstract_item import Item


@dataclass
class Genre(GenreCommon, Item):
    ...
