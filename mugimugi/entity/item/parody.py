from dataclasses import dataclass, field
from enum import Enum
from typing import Iterator, Union

from ...enum import Ratio
from ..abstract import Element
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
class AbstractParody(Element):
    class Type(Enum):
        TYPE = ItemType.PARODY

    _id: str = field(
        default=None,
        metadata=dict(
            name="ID",
            type=XmlType.ATTRIBUTE,
            required=True,
            pattern=fr"{ElementPrefix.PARODY.value}\d+",
        ),
    )
    # Used as discriminator
    _type: Type = field(
        default=Type.TYPE,
        metadata=dict(name="TYPE", type=XmlType.ATTRIBUTE, required=True),
    )
    prefix: ElementPrefix = ElementPrefix.PARODY
    type: ItemType = ItemType.PARODY


@dataclass
class Parody(AbstractParody, LinkableItem[LI]):
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
    def characters(self) -> Iterator[LinkedCharacter]:
        type_ = ItemType.CHARACTER
        for e in self._links.items:
            if e.type is type_:
                yield e


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
