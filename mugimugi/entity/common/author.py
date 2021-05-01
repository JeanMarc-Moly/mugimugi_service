from dataclasses import dataclass, field
from enum import Enum

from xsdata.formats.dataclass.models.elements import XmlType

from .abstract import ElementPrefix
from .abstract_item import ItemCommon, ItemType


@dataclass
class AuthorCommon(ItemCommon):
    class Type(Enum):
        TYPE = ItemType.AUTHOR

    mugimugi_id: str = field(
        default=None,
        metadata=dict(
            name="ID",
            type=XmlType.ATTRIBUTE,
            required=True,
            pattern=fr"{ElementPrefix.AUTHOR.value}\d+",
        ),
    )
    # Used as discriminator
    _type: Type = field(
        default=Type.TYPE,
        metadata=dict(name="TYPE", type=XmlType.ATTRIBUTE, required=True),
    )
    type: ItemType = ItemType.AUTHOR
    parent: int = field(
        default=0,
        metadata=dict(
            name="PARENT", type=XmlType.ATTRIBUTE, required=True, min_inclusive=0
        ),
    )

    @classmethod
    @property
    def PREFIX(cls) -> ElementPrefix:
        return ElementPrefix.AUTHOR
