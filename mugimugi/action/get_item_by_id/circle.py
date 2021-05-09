from dataclasses import dataclass, field

from xsdata.formats.dataclass.models.elements import XmlType

from ...entity.main import Circle
from ...entity.root import ValidRoot
from ...enum.element_prefix import ElementPrefix
from .abstract import GetItemById


@dataclass
class GetCircleById(GetItemById):
    @dataclass
    class Root(ValidRoot[Circle]):
        elements: list[Circle] = field(
            default_factory=list,
            metadata=dict(name=Circle.Meta.name, type=XmlType.ELEMENT, min_occurs=0),
        )

    root: Root = field(default=Root, init=False)

    @classmethod
    @property
    def PREFIX(cls) -> ElementPrefix:
        return Circle.PREFIX
