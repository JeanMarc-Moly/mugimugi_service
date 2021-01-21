from dataclasses import dataclass, field
from enum import Enum

from ..root import ValidRoot, XmlType
from .abstract import ElementPrefix, Item, ItemType, LinkedPartialItem


@dataclass
class AbstractImprint:
    class Type(Enum):
        TYPE = ItemType.IMPRINT

    id: str = field(
        default=None,
        metadata=dict(
            name="ID",
            type=XmlType.ATTRIBUTE,
            required=True,
            pattern=fr"{ElementPrefix.IMPRINT.value}\d+",
        ),
    )
    # Used as discriminator
    _type: Type = field(
        default=Type.TYPE,
        metadata=dict(name="TYPE", type=XmlType.ATTRIBUTE, required=True),
    )


@dataclass
class Imprint(AbstractImprint, Item):
    ...


@dataclass
class ImprintRoot(ValidRoot[Imprint]):
    elements: list[Imprint] = field(
        default_factory=list,
        metadata=dict(name=Imprint.Meta.name, type=XmlType.ELEMENT, min_occurs=0),
    )


@dataclass
class LinkedPartialImprint(AbstractImprint, LinkedPartialItem):
    # FRQ present but useless
    _frq: int = field(
        init=False,
        default=0,
        metadata=dict(name="FRQ", type=XmlType.ATTRIBUTE, required=True),
    )
