from dataclasses import dataclass, field
from enum import Enum

from ..root import ValidRoot, XmlType
from .abstract import ElementPrefix, Item, ItemType, LinkedPartialItem


@dataclass
class AbstractPublisher:
    class Type(Enum):
        TYPE = ItemType.PUBLISHER

    id: str = field(
        default=None,
        metadata=dict(
            name="ID",
            type=XmlType.ATTRIBUTE,
            required=True,
            pattern=fr"{ElementPrefix.PUBLISHER.value}\d+",
        ),
    )
    # Used as discriminator
    _type: Type = field(
        default=Type.TYPE,
        metadata=dict(name="TYPE", type=XmlType.ATTRIBUTE, required=True),
    )


@dataclass
class Publisher(AbstractPublisher, Item):
    ...


@dataclass
class PublisherRoot(ValidRoot[Publisher]):
    elements: list[Publisher] = field(
        default_factory=list,
        metadata=dict(name=Publisher.Meta.name, type=XmlType.ELEMENT, min_occurs=0),
    )


@dataclass
class LinkedPartialPublisher(AbstractPublisher, LinkedPartialItem):
    # FRQ present but useless
    _frq: int = field(
        init=False,
        default=0,
        metadata=dict(name="FRQ", type=XmlType.ATTRIBUTE, required=True),
    )
