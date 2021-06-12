from dataclasses import dataclass, field

from xsdata.formats.dataclass.models.elements import XmlType

from ...entity.main import Author
from ...entity.root import ValidRoot
from ...enum import ElementPrefix, ItemType
from .abstract import SearchItem


@dataclass
class SearchAuthor(SearchItem):
    @dataclass
    class Root(ValidRoot[Author]):
        elements: list[Author] = field(
            default_factory=list,
            metadata=dict(name=Author.Meta.name, type=XmlType.ELEMENT, min_occurs=0),
        )

    root: Root = field(default=Root, init=False)
    type_: ItemType = field(default=ItemType.AUTHOR, init=False)

    @classmethod
    @property
    def PREFIX(cls) -> ElementPrefix:
        return Author.PREFIX
