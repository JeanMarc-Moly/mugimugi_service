from dataclasses import dataclass, field

from xsdata.formats.dataclass.models.elements import XmlType

from ...entity.main import Genre
from ...entity.root import ValidRoot
from ...enum import ElementPrefix, ItemType
from .abstract import SearchItem


@dataclass
class SearchGenre(SearchItem):
    @dataclass
    class Root(ValidRoot[Genre]):
        elements: list[Genre] = field(
            default_factory=list,
            metadata=dict(name=Genre.Meta.name, type=XmlType.ELEMENT, min_occurs=0),
        )

    root: Root = field(default=Root, init=False)
    type_: ItemType = field(default=ItemType.GENRE, init=False)

    @classmethod
    @property
    def PREFIX(cls) -> ElementPrefix:
        return Genre.PREFIX
