from dataclasses import dataclass, field
from enum import Enum

from xsdata.formats.dataclass.models.elements import XmlType

from .abstract import ElementPrefix
from .abstract_item import ItemCommon, ItemType


@dataclass
class TypeCommon(ItemCommon):
    class Type(Enum):
        TYPE = ItemType.TYPE

    mugimugi_id: str = field(
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
