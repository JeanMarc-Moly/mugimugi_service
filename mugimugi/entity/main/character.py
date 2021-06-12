from dataclasses import dataclass, field
from typing import Iterator

from xsdata.formats.dataclass.models.elements import XmlType

from ..common import CharacterCommon
from .abstract_item import Item, LinkableItem
from .abstract_linker import AbstractLinker
from .sub import SubContent


@dataclass
class Character(CharacterCommon, LinkableItem[SubContent]):
    @dataclass
    class Linker(AbstractLinker):
        items: list[SubContent] = field(
            default_factory=list,
            metadata=dict(name=Item.Meta.name, type=XmlType.ELEMENT, min_occurs=0),
        )

    _links: Linker = field(
        default=None,
        metadata=dict(
            name=AbstractLinker.Meta.name, type=XmlType.ELEMENT, min_occurs=0
        ),
    )

    @property
    def contents(self) -> Iterator[SubContent]:
        yield from self._links.items
