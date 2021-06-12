from dataclasses import dataclass, field
from typing import Generic, Iterator, TypeVar

from xsdata.formats.dataclass.models.elements import XmlType

from ..common import ItemCommon
from .abstract_linker import AbstractLinker
from .sub import SubItem

LI = TypeVar("LI", bound=SubItem)


class LinkableItem(ItemCommon, Generic[LI]):
    _links: AbstractLinker

    @property
    def items(self) -> Iterator[LI]:
        for e in self._links.items:
            yield e


@dataclass
class Item(ItemCommon):
    # Useless but present.
    _: AbstractLinker = field(
        default=None, metadata=dict(name=AbstractLinker.Meta.name, type=XmlType.ELEMENT)
    )
