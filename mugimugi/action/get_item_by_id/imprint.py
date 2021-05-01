from dataclasses import dataclass, field
from typing import Iterable

from xsdata.formats.dataclass.models.elements import XmlType

from ...entity.main import Imprint
from ...entity.root import ValidRoot
from ...enum.element_prefix import ElementPrefix
from .abstract import GetItemById


class GetImprintById(GetItemById):
    @dataclass
    class Root(ValidRoot[Imprint]):
        elements: list[Imprint] = field(
            default_factory=list,
            metadata=dict(name=Imprint.Meta.name, type=XmlType.ELEMENT, min_occurs=0),
        )

    def __init__(self, ids: Iterable[int]):
        super().__init__(self.Root, ids)

    @classmethod
    @property
    def PREFIX(cls) -> ElementPrefix:
        return Imprint.PREFIX
