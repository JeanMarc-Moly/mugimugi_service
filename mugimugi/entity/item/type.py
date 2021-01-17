from dataclasses import dataclass, field

from ..root import XmlType
from .abstract import ElementPrefix, ItemType, LinkedPartialItem


@dataclass
class AbstractType:
    id: str = field(
        default=None,
        metadata=dict(
            name="ID",
            type=XmlType.ATTRIBUTE,
            required=True,
            pattern=fr"{ElementPrefix.TYPE.value}\d+",
        ),
    )
    type: ItemType = field(
        init=False,
        default=ItemType.TYPE,
        metadata=dict(name="TYPE", type=XmlType.ATTRIBUTE, required=True),
    )


@dataclass
class LinkedPartialType(AbstractType, LinkedPartialItem):
    # FRQ present but useless
    _frq: int = field(
        init=False,
        default=0,
        metadata=dict(name="FRQ", type=XmlType.ATTRIBUTE, required=True),
    )
