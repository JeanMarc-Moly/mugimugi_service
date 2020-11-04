from dataclasses import dataclass, field

from ..root import ValidRoot, XmlType
from .abstract import ElementPrefix, Item, ItemType, LinkedPartialItem


@dataclass
class AbstractImprint:
    id: str = field(
        default=None,
        metadata=dict(
            name="ID",
            type=XmlType.ATTRIBUTE,
            required=True,
            pattern=fr"{ElementPrefix.IMPRINT.value}\d+",
        ),
    )
    type: ItemType = field(
        init=False,
        default=ItemType.IMPRINT,
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
    ...
