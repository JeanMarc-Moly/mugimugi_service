from dataclasses import dataclass, field
from enum import Enum

from xsdata.formats.dataclass.models.elements import XmlType

from ..utils.converter import Date
from .abstract import ElementPrefix
from .abstract_item import ItemCommon, ItemType


@dataclass
class ConventionCommon(ItemCommon):
    class Type(Enum):
        TYPE = ItemType.CONVENTION

    mugimugi_id: str = field(
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
    prefix: ElementPrefix = ElementPrefix.CONVENTION
    type: ItemType = ItemType.CONVENTION
    date_start: Date = field(
        default=None,
        metadata=dict(name="DATE_START", type=XmlType.ELEMENT, required=True),
    )
    date_end: Date = field(
        default=None,
        metadata=dict(name="DATE_END", type=XmlType.ELEMENT, required=True),
    )

    @classmethod
    @property
    def PREFIX(cls) -> ElementPrefix:
        return ElementPrefix.CONVENTION
