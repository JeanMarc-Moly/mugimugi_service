from dataclasses import dataclass, field

from xsdata.formats.dataclass.models.elements import XmlType

from ...entity.main import Character
from ...entity.root import ValidRoot
from ...enum import ElementPrefix, ItemType
from .abstract import SearchItem


@dataclass
class SearchCharacter(SearchItem):
    @dataclass
    class Root(ValidRoot[Character]):
        elements: list[Character] = field(
            default_factory=list,
            metadata=dict(name=Character.Meta.name, type=XmlType.ELEMENT, min_occurs=0),
        )

    root: Root = field(default=Root, init=False)
    type_: ItemType = field(default=ItemType.CHARACTER, init=False)

    @classmethod
    @property
    def PREFIX(cls) -> ElementPrefix:
        return Character.PREFIX
