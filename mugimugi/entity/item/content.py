from dataclasses import dataclass, field
from enum import Enum

from ...enum import Ratio
from ..root import ValidRoot, XmlType
from .abstract import ElementPrefix, Item, ItemType, LinkedItem, LinkedPartialItem


@dataclass
class AbstractContent:
    class Type(Enum):
        TYPE = ItemType.CONTENT

    id: str = field(
        default=None,
        metadata=dict(
            name="ID",
            type=XmlType.ATTRIBUTE,
            required=True,
            pattern=fr"{ElementPrefix.CONTENT.value}\d+",
        ),
    )
    # Used as discriminator
    _type: Type = field(
        default=Type.TYPE,
        metadata=dict(name="TYPE", type=XmlType.ATTRIBUTE, required=True),
    )


@dataclass
class Content(AbstractContent, Item):
    ...


@dataclass
class ContentRoot(ValidRoot[Content]):
    elements: list[Content] = field(
        default_factory=list,
        metadata=dict(name=Content.Meta.name, type=XmlType.ELEMENT, min_occurs=0),
    )


@dataclass
class LinkedContent(AbstractContent, LinkedItem):
    ...


@dataclass
class LinkedPartialContent(AbstractContent, LinkedPartialItem):
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
