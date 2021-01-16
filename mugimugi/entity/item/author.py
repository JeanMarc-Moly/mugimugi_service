from dataclasses import dataclass, field
from typing import Iterator

from ...enum import Position
from ..root import ValidRoot, XmlType
from .abstract import (
    AbstractLinker,
    ElementPrefix,
    Item,
    ItemType,
    LinkableItem,
    LinkedItem,
    LinkedPartialItem,
)
from .content import LinkedContent


@dataclass
class Linker(AbstractLinker[LinkedContent]):
    items: list[LinkedContent] = field(
        default_factory=list,
        metadata=dict(name=Item.Meta.name, type=XmlType.ELEMENT, min_occurs=0),
    )


@dataclass
class AbstractAuthor:
    id: str = field(
        default=None,
        metadata=dict(
            name="ID",
            type=XmlType.ATTRIBUTE,
            required=True,
            pattern=fr"{ElementPrefix.AUTHOR.value}\d+",
        ),
    )
    type: ItemType = field(
        init=False,
        default=ItemType.AUTHOR,
        metadata=dict(name="TYPE", type=XmlType.ATTRIBUTE, required=True),
    )
    parent: int = field(
        default=None,
        metadata=dict(
            name="PARENT", type=XmlType.ATTRIBUTE, required=True, min_inclusive=0
        ),
    )

    @property
    def contents(self) -> Iterator[LinkedContent]:
        yield from self.items


@dataclass
class Author(AbstractAuthor, LinkableItem[LinkedContent]):
    _links: Linker = field(
        default=None, metadata=dict(name="LINKS", type=XmlType.ELEMENT, min_occurs=0)
    )


@dataclass
class AuthorRoot(ValidRoot[Author]):
    elements: list[Author] = field(
        default_factory=list,
        metadata=dict(name=Author.Meta.name, type=XmlType.ELEMENT, min_occurs=0),
    )


@dataclass
class LinkedAuthor(AbstractAuthor, LinkedItem):
    ...


@dataclass
class LinkedPartialAuthor(AbstractAuthor, LinkedPartialItem):
    position: Position = field(
        default=None,
        metadata=dict(
            name="FRQ",
            type=XmlType.ATTRIBUTE,
            required=True,
            min_inclusive=0,
            max_inclusive=2,
        ),
    )
