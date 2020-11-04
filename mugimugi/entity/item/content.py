from dataclasses import dataclass, field

from ..root import ValidRoot, XmlType
from .abstract import ElementPrefix, Item, ItemType, LinkedItem, LinkedPartialItem


@dataclass
class AbstractContent:
    id: str = field(
        default=None,
        metadata=dict(
            name="ID",
            type=XmlType.ATTRIBUTE,
            required=True,
            pattern=fr"{ElementPrefix.CONTENT.value}\d+",
        ),
    )
    type: ItemType = field(
        init=False,
        default=ItemType.CONTENT,
        metadata=dict(name="TYPE", type=XmlType.ATTRIBUTE, required=True),
    )


@dataclass
class Content(AbstractContent, Item):
    ...


@dataclass
class ContentRoot(ValidRoot[Content]):
    elements: list[Content] = field(
        default_factory=list,
        metadata=dict(name=Content.Meta.name, type=XmlType.ELEMENT, min_occurs=0),
    )


@dataclass
class LinkedContent(AbstractContent, LinkedItem):
    ...


@dataclass
class LinkedPartialContent(AbstractContent, LinkedPartialItem):
    ...
