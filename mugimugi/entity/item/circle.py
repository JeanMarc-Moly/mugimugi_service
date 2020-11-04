from dataclasses import dataclass, field
from typing import Iterator, Union

from ..root import ValidRoot, XmlType
from .abstract import (
    AbstractLinker,
    ElementPrefix,
    Item,
    ItemType,
    LinkableItem,
    LinkedPartialItem,
)
from .author import LinkedAuthor
from .content import LinkedContent


LI = Union[LinkedContent, LinkedAuthor]


@dataclass
class Linker(AbstractLinker[LI]):
    items: list[LI] = field(
        default_factory=list,
        metadata=dict(name=Item.Meta.name, type=XmlType.ELEMENT, min_occurs=0),
    )


@dataclass
class AbstractCircle:
    id: str = field(
        default=None,
        metadata=dict(
            name="ID",
            type=XmlType.ATTRIBUTE,
            required=True,
            pattern=fr"{ElementPrefix.CIRCLE.value}\d+",
        ),
    )
    type: ItemType = field(
        init=False,
        default=ItemType.CIRCLE,
        metadata=dict(name="TYPE", type=XmlType.ATTRIBUTE, required=True),
    )
    parent: int = field(
        default=None,
        metadata=dict(
            name="PARENT", type=XmlType.ATTRIBUTE, required=True, min_inclusive=0
        ),
    )

    @property
    def contents(self) -> Iterator[LinkedContent]:
        for e in self.items:
            if e.type is ItemType.CONTENT:
                yield e

    @property
    def authors(self) -> Iterator[LinkedAuthor]:
        for e in self.items:
            if e.type is ItemType.AUTHOR:
                yield e


@dataclass
class Circle(AbstractCircle, LinkableItem[LI]):
    _links: Linker = field(
        default=None, metadata=dict(name="LINKS", type=XmlType.ELEMENT, min_occurs=0)
    )


@dataclass
class CircleRoot(ValidRoot[Circle]):
    elements: list[Circle] = field(
        default_factory=list,
        metadata=dict(name=Circle.Meta.name, type=XmlType.ELEMENT, min_occurs=0),
    )


@dataclass
class LinkedPartialCircle(AbstractCircle, LinkedPartialItem):
    ...
