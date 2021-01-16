from dataclasses import dataclass, field
from typing import Iterator, Union

from ...enum import Ratio
from ..root import ValidRoot, XmlType
from .abstract import (
    AbstractLinker,
    ElementPrefix,
    Item,
    ItemType,
    LinkableItem,
    LinkedItem,
    LinkedPartialItem,
)
from .character import LinkedCharacter
from .content import LinkedContent

LI = Union[LinkedContent, LinkedCharacter]


@dataclass
class Linker(AbstractLinker[LI]):
    items: list[LI] = field(
        default_factory=list,
        metadata=dict(name=Item.Meta.name, type=XmlType.ELEMENT, min_occurs=0),
    )


@dataclass
class AbstractParody:
    id: str = field(
        default=None,
        metadata=dict(
            name="ID",
            type=XmlType.ATTRIBUTE,
            required=True,
            pattern=fr"{ElementPrefix.PARODY.value}\d+",
        ),
    )
    type: ItemType = field(
        init=False,
        default=ItemType.PARODY,
        metadata=dict(name="TYPE", type=XmlType.ATTRIBUTE, required=True),
    )

    @property
    def contents(self) -> Iterator[LinkedContent]:
        for e in self.items:
            if e.type is ItemType.CONTENT:
                yield e

    @property
    def characters(self) -> Iterator[LinkedCharacter]:
        for e in self.items:
            if e.type is ItemType.CHARACTER:
                yield e


@dataclass
class Parody(AbstractParody, LinkableItem[LI]):
    _links: Linker = field(
        default=None, metadata=dict(name="LINKS", type=XmlType.ELEMENT, min_occurs=0)
    )


@dataclass
class ParodyRoot(ValidRoot[Parody]):
    elements: list[Parody] = field(
        default_factory=list,
        metadata=dict(name=Parody.Meta.name, type=XmlType.ELEMENT, min_occurs=0),
    )


@dataclass
class LinkedParody(AbstractParody, LinkedItem):
    ...


@dataclass
class LinkedPartialParody(AbstractParody, LinkedPartialItem):
    ratio: Ratio = field(
        default=None,
        metadata=dict(
            name="FRQ",
            type=XmlType.ATTRIBUTE,
            required=True,
            min_inclusive=0,
            max_inclusive=5,
        ),
    )
