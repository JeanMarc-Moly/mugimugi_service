from dataclasses import dataclass, field
from enum import Enum

from xsdata.formats.dataclass.models.elements import XmlType

from mugimugi.enum.gender import Sex

from .abstract import ElementPrefix
from .abstract_item import ItemCommon, ItemType


@dataclass
class CharacterCommon(ItemCommon):
    class Type(Enum):
        TYPE = ItemType.CHARACTER

    mugimugi_id: str = field(
        default=None,
        metadata=dict(
            name="ID",
            type=XmlType.ATTRIBUTE,
            required=True,
            pattern=fr"{ElementPrefix.CHARACTER.value}\d+",
        ),
    )
    # Used as discriminator
    _type: Type = field(
        default=Type.TYPE,
        metadata=dict(name="TYPE", type=XmlType.ATTRIBUTE, required=True),
    )
    prefix: ElementPrefix = ElementPrefix.CHARACTER
    type: ItemType = ItemType.CHARACTER
    sex: Sex = field(
        default=None,
        metadata=dict(
            name="DATA_SEX",
            type=XmlType.ELEMENT,
            required=True,
            min_inclusive=0,
            max_inclusive=4,
        ),
    )
    age: str = field(
        default=None,
        metadata=dict(name="DATA_AGE", type=XmlType.ELEMENT, required=True),
    )

    @classmethod
    @property
    def PREFIX(self) -> ElementPrefix:
        return ElementPrefix.CHARACTER
