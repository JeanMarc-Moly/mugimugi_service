from dataclasses import dataclass, field
from typing import Iterable

from xsdata.formats.dataclass.models.elements import XmlType

from ...entity.main import Publisher
from ...entity.root import ValidRoot
from ...enum.element_prefix import ElementPrefix
from .abstract import GetItemById


class GetPublisherById(GetItemById):
    @dataclass
    class Root(ValidRoot[Publisher]):
        elements: list[Publisher] = field(
            default_factory=list,
            metadata=dict(name=Publisher.Meta.name, type=XmlType.ELEMENT, min_occurs=0),
        )

    def __init__(self, ids: Iterable[int]):
        super().__init__(self.Root, ids)

    @classmethod
    @property
    def PREFIX(self) -> ElementPrefix:
        return Publisher.PREFIX
