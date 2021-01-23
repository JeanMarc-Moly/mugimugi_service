from dataclasses import dataclass, field
from enum import Enum

from ..abstract import Element
from ..root import XmlType
from .abstract import ElementPrefix, ItemType, LinkedPartialItem


@dataclass
class AbstractType(Element):
    class Type(Enum):
        TYPE = ItemType.TYPE

    _id: str = field(
        default=None,
        metadata=dict(
            name="ID",
            type=XmlType.ATTRIBUTE,
            required=True,
            pattern=fr"{ElementPrefix.TYPE.value}\d+",
        ),
    )
    # Used as discriminator
    _type: Type = field(
        default=Type.TYPE,
        metadata=dict(name="TYPE", type=XmlType.ATTRIBUTE, required=True),
    )
    prefix: ElementPrefix = ElementPrefix.TYPE
    type: ItemType = ItemType.TYPE


@dataclass
class LinkedPartialType(AbstractType, LinkedPartialItem):
    # FRQ present but useless
    _: int = field(
        init=False,
        default=0,
        metadata=dict(name="FRQ", type=XmlType.ATTRIBUTE, required=True),
    )
