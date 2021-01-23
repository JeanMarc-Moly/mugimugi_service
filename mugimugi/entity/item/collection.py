from dataclasses import dataclass, field
from enum import Enum

from ..abstract import Element
from ..root import ValidRoot, XmlType
from .abstract import ElementPrefix, Item, ItemType, LinkedPartialItem


@dataclass
class AbstractCollection(Element):
    class Type(Enum):
        TYPE = ItemType.COLLECTION

    _id: str = field(
        default=None,
        metadata=dict(
            name="ID",
            type=XmlType.ATTRIBUTE,
            required=True,
            pattern=fr"{ElementPrefix.COLLECTION.value}\d+",
        ),
    )
    # Used as discriminator
    _type: Type = field(
        default=Type.TYPE,
        metadata=dict(name="TYPE", type=XmlType.ATTRIBUTE, required=True),
    )
    prefix: ElementPrefix = ElementPrefix.COLLECTION
    type: ItemType = ItemType.COLLECTION


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
    # FRQ present but useless
    _: int = field(
        init=False,
        default=0,
        metadata=dict(name="FRQ", type=XmlType.ATTRIBUTE, required=True),
    )
