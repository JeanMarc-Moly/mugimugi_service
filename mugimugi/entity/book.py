from dataclasses import dataclass, field
from datetime import date
from typing import Iterator, Union

from ..enum import ElementPrefix, Language
from ..enum.element_node import ElementNode
from .abstract import Element
from .converter import Percent
from .item import (
    LinkedPartialAuthor,
    LinkedPartialCharacter,
    LinkedPartialCircle,
    LinkedPartialCollection,
    LinkedPartialContent,
    LinkedPartialConvention,
    LinkedPartialGenre,
    LinkedPartialImprint,
    LinkedPartialParody,
    LinkedPartialPublisher,
    LinkedPartialType,
)
from .item.abstract import Item
from .root import ValidRoot, XmlType

LI = Union[
    LinkedPartialAuthor,
    LinkedPartialCharacter,
    LinkedPartialCircle,
    LinkedPartialCollection,
    LinkedPartialContent,
    LinkedPartialConvention,
    LinkedPartialGenre,
    LinkedPartialImprint,
    LinkedPartialParody,
    LinkedPartialPublisher,
    LinkedPartialType,
]


@dataclass
class Linker:
    items: list[LI] = field(
        default_factory=list,
        metadata=dict(name=Item.Meta.name, type=XmlType.ELEMENT, min_occurs=0),
    )


@dataclass
class Book(ManyNamesElement):
    class Meta:
        name = ElementNode.BOOK.value

    id: str = field(
        default=None,
        metadata=dict(
            name="ID",
            type=XmlType.ATTRIBUTE,
            required=True,
            pattern=fr"{ElementPrefix.BOOK.value}\d+",
        ),
    )
    prefix: ElementPrefix = ElementPrefix.BOOK
    version: int = field(
        default=None,
        metadata=dict(
            name="VER", type=XmlType.ATTRIBUTE, required=True, min_inclusive=0
        ),
    )
    match_ratio: Percent = field(
        default=None,
        metadata=dict(
            name="search", type=XmlType.ATTRIBUTE, required=True, min_inclusive=0
        ),
    )
    release_date: date = field(
        default=None,
        metadata=dict(
            name="DATE_RELEASED", type=XmlType.ELEMENT, required=True, format="%Y-%m-%d"
        ),
    )
    isbn: str = field(
        default=None,
        metadata=dict(name="DATA_ISBN", type=XmlType.ELEMENT, required=True),
    )
    pages_count: int = field(
        default=None,
        metadata=dict(name="DATA_PAGES", type=XmlType.ELEMENT, required=True),
    )
    is_adult: bool = field(
        default=False,
        metadata=dict(name="DATA_AGE", type=XmlType.ELEMENT, required=True),
    )
    is_anthology: bool = field(
        default=False,
        metadata=dict(name="DATA_ANTHOLOGY", type=XmlType.ELEMENT, required=True),
    )
    is_copybook: bool = field(
        default=False,
        metadata=dict(name="DATA_COPYSHI", type=XmlType.ELEMENT, required=True),
    )
    magazine: int = field(
        default=None,
        metadata=dict(name="DATA_MAGAZINE", type=XmlType.ELEMENT, required=True),
    )
    language: Language = field(
        default=None,
        metadata=dict(name="DATA_LANGUAGE", type=XmlType.ELEMENT, required=True),
    )
    info: str = field(
        default=None,
        metadata=dict(name="DATA_INFO", type=XmlType.ELEMENT, required=True),
    )
    _links: Linker = field(
        default=None, metadata=dict(name="LINKS", type=XmlType.ELEMENT)
    )

    @property
    def items(self) -> Iterator[LI]:
        for e in self._links.items:
            yield e


@dataclass
class BookRoot(ValidRoot[Book]):
    elements: list[Book] = field(
        default_factory=list,
        metadata=dict(name=Book.Meta.name, type=XmlType.ELEMENT, min_occurs=0),
    )
