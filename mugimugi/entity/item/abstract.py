from dataclasses import dataclass, field
from typing import Generic, Iterator, TypeVar
from ...enum import ElementPrefix, Share, ItemType, ElementNode
from ..root import ManyNamesElement, XmlType


@dataclass
class AbstractItem(ManyNamesElement):
    class Meta:
        name = ElementNode.ITEM.value

    id: str = field(
        default=None,
        metadata=dict(
            name="ID",
            type=XmlType.ATTRIBUTE,
            required=True,
            pattern=fr"[{''.join(ElementPrefix.values())}]\d+",
        ),
    )
    version: int = field(
        default=None,
        metadata=dict(
            name="VER", type=XmlType.ATTRIBUTE, required=True, min_inclusive=0
        ),
    )
    type: ItemType = field(
        default=None, metadata=dict(name="TYPE", type=XmlType.ATTRIBUTE, required=True)
    )
    objects_count: int = field(
        default=None,
        metadata=dict(
            name="OBJECTS", type=XmlType.ELEMENT, required=True, min_inclusive=0
        ),
    )

    @property
    def bare_id(self) -> int:
        return int(self.id[1:])


@dataclass
class LinkedItem(AbstractItem):
    ...


@dataclass
class LinkedPartialItem(AbstractItem):
    ratio: Share = field(
        default=None,
        metadata=dict(
            name="FRQ",
            type=XmlType.ATTRIBUTE,
            required=True,
            min_inclusive=0,
            max_inclusive=5,
        ),
    )


LI = TypeVar("LI", bound=LinkedItem)


class AbstractLinker(Generic[LI]):
    items: list[LI]


class LinkableItem(AbstractItem, Generic[LI]):
    _links: AbstractLinker[LI]

    @property
    def items(self) -> Iterator[LI]:
        for e in self._links.items:
            yield e


@dataclass
class Item(AbstractItem):
    _links: AbstractLinker[None] = field(
        default=None, metadata=dict(name="LINKS", type=XmlType.ELEMENT)
    )
