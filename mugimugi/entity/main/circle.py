from dataclasses import dataclass, field
from typing import Iterator, Union

from xsdata.formats.dataclass.models.elements import XmlType

from mugimugi.enum.item_type import ItemType

from ..common import CircleCommon
from .abstract_item import Item, LinkableItem
from .abstract_linker import AbstractLinker
from .sub import SubAuthor, SubContent

LI = Union[SubAuthor, SubContent]


@dataclass
class Circle(CircleCommon, LinkableItem[LI]):
    @dataclass
    class Linker(AbstractLinker):
        items: list[LI] = field(
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
        type_ = ItemType.CONTENT
        for e in self._links.items:
            if e.type is type_:
                yield e

    @property
    def contents(self) -> Iterator[SubAuthor]:
        type_ = ItemType.AUTHOR
        for e in self._links.items:
            if e.type is type_:
                yield e
