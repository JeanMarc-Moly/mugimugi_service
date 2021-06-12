from dataclasses import dataclass, field

from xsdata.formats.dataclass.models.elements import XmlType

from ...entity.main import Parody
from ...entity.root import ValidRoot
from ...enum import ElementPrefix, ItemType
from .abstract import SearchItem


@dataclass
class SearchParody(SearchItem):
    @dataclass
    class Root(ValidRoot[Parody]):
        elements: list[Parody] = field(
            default_factory=list,
            metadata=dict(name=Parody.Meta.name, type=XmlType.ELEMENT, min_occurs=0),
        )

    root: Root = field(default=Root, init=False)
    type_: ItemType = field(default=ItemType.PARODY, init=False)

    @classmethod
    @property
    def PREFIX(cls) -> ElementPrefix:
        return Parody.PREFIX
