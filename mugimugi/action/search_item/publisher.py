from dataclasses import dataclass, field

from xsdata.formats.dataclass.models.elements import XmlType

from ...entity.main import Publisher
from ...entity.root import ValidRoot
from ...enum import ElementPrefix, ItemType
from .abstract import SearchItem


@dataclass
class SearchPublisher(SearchItem):
    @dataclass
    class Root(ValidRoot[Publisher]):
        elements: list[Publisher] = field(
            default_factory=list,
            metadata=dict(name=Publisher.Meta.name, type=XmlType.ELEMENT, min_occurs=0),
        )

    root: Root = field(default=Root, init=False)
    type_: ItemType = field(default=ItemType.PUBLISHER, init=False)

    @classmethod
    @property
    def PREFIX(cls) -> ElementPrefix:
        return Publisher.PREFIX
