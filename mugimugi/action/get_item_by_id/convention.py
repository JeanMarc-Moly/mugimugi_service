from dataclasses import dataclass, field

from xsdata.formats.dataclass.models.elements import XmlType

from ...entity.main import Convention
from ...entity.root import ValidRoot
from ...enum.element_prefix import ElementPrefix
from .abstract import GetItemById


@dataclass
class GetConventionById(GetItemById):
    @dataclass
    class Root(ValidRoot[Convention]):
        elements: list[Convention] = field(
            default_factory=list,
            metadata=dict(
                name=Convention.Meta.name, type=XmlType.ELEMENT, min_occurs=0
            ),
        )

    root: Root = field(default=Root, init=False)

    @classmethod
    @property
    def PREFIX(cls) -> ElementPrefix:
        return Convention.PREFIX
