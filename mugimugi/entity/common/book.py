from dataclasses import dataclass, field
from datetime import date

from xsdata.formats.dataclass.models.elements import XmlType

from mugimugi.entity.utils.converter.percent import Percent
from mugimugi.enum import ElementPrefix, Language
from mugimugi.enum.element_node import ElementNode

from .abstract import Element


@dataclass
class BookCommon(Element):
    class Meta:
        name = ElementNode.BOOK.value

    _id: str = field(
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
