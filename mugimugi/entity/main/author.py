from dataclasses import dataclass, field
from typing import Iterator

from xsdata.formats.dataclass.models.elements import XmlType

from ..common import AuthorCommon
from .abstract_item import LinkableItem
from .abstract_linker import AbstractLinker
from .sub import SubContent


@dataclass
class Author(AuthorCommon, LinkableItem[SubContent]):
    @dataclass
    class Linker(AbstractLinker):
        items: list[SubContent] = field(
            default_factory=list,
            metadata=dict(
                name=LinkableItem.Meta.name, type=XmlType.ELEMENT, min_occurs=0
            ),
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
