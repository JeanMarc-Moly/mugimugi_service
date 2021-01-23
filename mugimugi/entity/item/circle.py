from dataclasses import dataclass, field
from enum import Enum
from typing import Iterator, Union

from ...enum import Position
from ..abstract import Element
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
class AbstractCircle(Element):
    class Type(Enum):
        TYPE = ItemType.CIRCLE

    _id: str = field(
        default=None,
        metadata=dict(
            name="ID",
            type=XmlType.ATTRIBUTE,
            required=True,
            pattern=fr"{ElementPrefix.CIRCLE.value}\d+",
        ),
    )
    # Used as discriminator
    _type: Type = field(
        default=Type.TYPE,
        metadata=dict(name="TYPE", type=XmlType.ATTRIBUTE, required=True),
    )
    prefix: ElementPrefix = ElementPrefix.CIRCLE
    type: ItemType = ItemType.CIRCLE
    parent: int = field(
        default=None,
        metadata=dict(
            name="PARENT", type=XmlType.ATTRIBUTE, required=True, min_inclusive=0
        ),
    )


@dataclass
class Circle(AbstractCircle, LinkableItem[LI]):
    _links: Linker = field(
        default=None, metadata=dict(name="LINKS", type=XmlType.ELEMENT, min_occurs=0)
    )

    @property
    def contents(self) -> Iterator[LinkedContent]:
        type_ = ItemType.CONTENT
        for e in self._links.items:
            if e.type is type_:
                yield e

    @property
    def contents(self) -> Iterator[LinkedAuthor]:
        type_ = ItemType.AUTHOR
        for e in self._links.items:
            if e.type is type_:
                yield e


@dataclass
class CircleRoot(ValidRoot[Circle]):
    elements: list[Circle] = field(
        default_factory=list,
        metadata=dict(name=Circle.Meta.name, type=XmlType.ELEMENT, min_occurs=0),
    )


@dataclass
class LinkedPartialCircle(AbstractCircle, LinkedPartialItem):
    position: Position = field(
        default=None,
        metadata=dict(
            name="FRQ",
            type=XmlType.ATTRIBUTE,
            required=True,
            min_inclusive=0,
            max_inclusive=2,
        ),
    )
