from abc import abstractmethod
from dataclasses import dataclass, field

from xsdata.formats.dataclass.models.elements import XmlType

from ...enum import ElementNode, ElementPrefix, ItemType
from .abstract import Element


@dataclass
class ItemCommon(Element):
    class Meta:
        name = ElementNode.ITEM.value

    _type: ItemType = field(
        default=None, metadata=dict(name="TYPE", type=XmlType.ATTRIBUTE, required=True)
    )
    type: ItemType = None
    version: int = field(
        default=None,
        metadata=dict(
            name="VER", type=XmlType.ATTRIBUTE, required=True, min_inclusive=0
        ),
    )
    objects_count: int = field(
        default=None,
        metadata=dict(
            name="OBJECTS", type=XmlType.ELEMENT, required=True, min_inclusive=0
        ),
    )

    def __post_init__(self):
        super().__post_init__()
        if self.type is None:
            self.type = self._type.value

    @classmethod
    @property
    @abstractmethod
    def PREFIX(cls) -> ElementPrefix:
        ...
