from dataclasses import dataclass, field

from xsdata.formats.dataclass.models.elements import XmlType

from ...entity.main import Genre
from ...entity.root import ValidRoot
from ...enum.element_prefix import ElementPrefix
from .abstract import GetItemById


@dataclass
class GetGenreById(GetItemById):
    @dataclass
    class Root(ValidRoot[Genre]):
        elements: list[Genre] = field(
            default_factory=list,
            metadata=dict(name=Genre.Meta.name, type=XmlType.ELEMENT, min_occurs=0),
        )

    root: Root = field(default=Root, init=False)

    @classmethod
    @property
    def PREFIX(cls) -> ElementPrefix:
        return Genre.PREFIX
