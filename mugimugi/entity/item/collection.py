from dataclasses import dataclass, field

from ..root import ValidRoot, XmlType
from .abstract import ElementPrefix, Item, ItemType, LinkedPartialItem


@dataclass
class AbstractCollection:
    id: str = field(
        default=None,
        metadata=dict(
            name="ID",
            type=XmlType.ATTRIBUTE,
            required=True,
            pattern=fr"{ElementPrefix.COLLECTION.value}\d+",
        ),
    )
    type: ItemType = field(
        init=False,
        default=ItemType.COLLECTION,
        metadata=dict(name="TYPE", type=XmlType.ATTRIBUTE, required=True),
    )


@dataclass
class Collection(AbstractCollection, Item):
    ...


@dataclass
class CollectionRoot(ValidRoot[Collection]):
    elements: list[Collection] = field(
        default_factory=list,
        metadata=dict(name=Collection.Meta.name, type=XmlType.ELEMENT, min_occurs=0),
    )


@dataclass
class LinkedPartialCollection(AbstractCollection, LinkedPartialItem):
    ...
