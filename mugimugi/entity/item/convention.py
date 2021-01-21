from dataclasses import dataclass, field
from datetime import date
from enum import Enum
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
from .character import LinkedCharacter
from .content import LinkedContent
from .parody import LinkedParody

LI = Union[LinkedContent, LinkedParody, LinkedCharacter]


@dataclass
class Linker(AbstractLinker[LI]):
    items: list[LI] = field(
        default_factory=list,
        metadata=dict(name=Item.Meta.name, type=XmlType.ELEMENT, min_occurs=0),
    )


@dataclass
class AbstractConvention:
    class Type(Enum):
        TYPE = ItemType.CONVENTION

    id: str = field(
        default=None,
        metadata=dict(
            name="ID",
            type=XmlType.ATTRIBUTE,
            required=True,
            pattern=fr"{ElementPrefix.CONVENTION.value}\d+",
        ),
    )
    # Used as discriminator
    _type: Type = field(
        default=Type.TYPE,
        metadata=dict(name="TYPE", type=XmlType.ATTRIBUTE, required=True),
    )
    date_start: date = field(
        default=None,
        metadata=dict(
            name="DATE_START", type=XmlType.ELEMENT, required=True, format="%Y-%m-%d"
        ),
    )
    date_end: date = field(
        default=None,
        metadata=dict(
            name="DATE_END", type=XmlType.ELEMENT, required=True, format="%Y-%m-%d"
        ),
    )

    @property
    def contents(self) -> Iterator[LinkedContent]:
        for e in self.items:
            if e.type is ItemType.CONTENT:
                yield e

    @property
    def parodies(self) -> Iterator[LinkedParody]:
        for e in self.items:
            if e.type is ItemType.PARODY:
                yield e

    @property
    def characters(self) -> Iterator[LinkedCharacter]:
        for e in self.items:
            if e.type is ItemType.CHARACTER:
                yield e


@dataclass
class Convention(AbstractConvention, LinkableItem[LI]):
    _links: Linker = field(
        default=None, metadata=dict(name="LINKS", type=XmlType.ELEMENT)
    )


@dataclass
class ConventionRoot(ValidRoot[Convention]):
    elements: list[Convention] = field(
        default_factory=list,
        metadata=dict(name=Convention.Meta.name, type=XmlType.ELEMENT, min_occurs=0),
    )


@dataclass
class LinkedPartialConvention(AbstractConvention, LinkedPartialItem):
    # FRQ present but useless
    _frq: int = field(
        init=False,
        default=0,
        metadata=dict(name="FRQ", type=XmlType.ATTRIBUTE, required=True),
    )
