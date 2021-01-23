from dataclasses import dataclass, field
from typing import Generic, Iterator, TypeVar

from ...enum import ElementNode, ElementPrefix, ItemType
from ..abstract import Element
from ..root import XmlType


@dataclass
class AbstractItem(Element):
    class Meta:
        name = ElementNode.ITEM.value

    _id: str = field(
        default=None,
        metadata=dict(
            name="ID",
            type=XmlType.ATTRIBUTE,
            required=True,
            pattern=fr"[{''.join(ElementPrefix.values())}]\d+",
        ),
    )
    _type: ItemType = field(
        default=None, metadata=dict(name="TYPE", type=XmlType.ATTRIBUTE, required=True)
    )
    type: ItemType = None
    version: int = field(
        default=None,
        metadata=dict(
            name="VER", type=XmlType.ATTRIBUTE, required=True, min_inclusive=0
        ),
    )
    _type: ItemType = field(
        default=None, metadata=dict(name="TYPE", type=XmlType.ATTRIBUTE, required=True)
    )
    objects_count: int = field(
        default=None,
        metadata=dict(
            name="OBJECTS", type=XmlType.ELEMENT, required=True, min_inclusive=0
        ),
    )

    def __post_init__(self):
        super().__post_init__()
        if self.type is None:
            self.type = self._type.value


@dataclass
class LinkedItem(AbstractItem):
    ...


@dataclass
class LinkedPartialItem(AbstractItem):
    ...


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
