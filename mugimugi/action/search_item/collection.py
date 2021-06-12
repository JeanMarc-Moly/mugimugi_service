from dataclasses import dataclass, field

from xsdata.formats.dataclass.models.elements import XmlType

from ...entity.main import Collection
from ...entity.root import ValidRoot
from ...enum import ElementPrefix, ItemType
from .abstract import SearchItem


@dataclass
class SearchCollection(SearchItem):
    @dataclass
    class Root(ValidRoot[Collection]):
        elements: list[Collection] = field(
            default_factory=list,
            metadata=dict(
                name=Collection.Meta.name, type=XmlType.ELEMENT, min_occurs=0
            ),
        )

    root: Root = field(default=Root, init=False)
    type_: ItemType = field(default=ItemType.COLLECTION, init=False)

    @classmethod
    @property
    def PREFIX(cls) -> ElementPrefix:
        return Collection.PREFIX
