from dataclasses import dataclass, field
from enum import Enum

from xsdata.formats.dataclass.models.elements import XmlType

from .abstract import ElementPrefix
from .abstract_item import ItemCommon, ItemType


@dataclass
class ParodyCommon(ItemCommon):
    class Type(Enum):
        TYPE = ItemType.PARODY

    mugimugi_id: str = field(
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

    @classmethod
    @property
    def PREFIX(cls) -> ElementPrefix:
        return ElementPrefix.PARODY
