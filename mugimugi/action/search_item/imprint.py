from dataclasses import dataclass, field

from xsdata.formats.dataclass.models.elements import XmlType

from ...entity.main import Imprint
from ...entity.root import ValidRoot
from ...enum import ElementPrefix, ItemType
from .abstract import SearchItem


@dataclass
class SearchImprint(SearchItem):
    @dataclass
    class Root(ValidRoot[Imprint]):
        elements: list[Imprint] = field(
            default_factory=list,
            metadata=dict(name=Imprint.Meta.name, type=XmlType.ELEMENT, min_occurs=0),
        )

    root: Root = field(default=Root, init=False)
    type_: ItemType = field(default=ItemType.IMPRINT, init=False)

    @classmethod
    @property
    def PREFIX(cls) -> ElementPrefix:
        return Imprint.PREFIX
