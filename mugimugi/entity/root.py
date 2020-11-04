from abc import ABC
from dataclasses import dataclass, field
from typing import Generic, Iterator, TypeVar

from xsdata.formats.dataclass.models.constants import XmlType
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.parsers.config import ParserConfig
from xsdata.formats.dataclass.parsers.nodes import ParserError

from ..enum import ElementNode
from .error import Error
from .user import User

PARSER = XmlParser(config=ParserConfig(fail_on_unknown_properties=True)).from_string


@dataclass
class AbstractRoot(ABC):
    class Meta:
        name = ElementNode.LIST.value

    @classmethod
    def parse(cls, xml: str):
        try:
            return PARSER(xml, cls)
        except ParserError as e:
            raise TypeError(f"Failed to parse: {e}")


@dataclass
class EmptyRoot(AbstractRoot):
    user: User = field(
        metadata=dict(name=User.Meta.name, type=XmlType.ELEMENT, required=True)
    )


E = TypeVar("E")


@dataclass
class ValidRoot(EmptyRoot, Generic[E]):
    elements: list[E]


@dataclass
class FailedRoot(AbstractRoot):
    error: Error = field(
        metadata=dict(name=Error.Meta.name, type=XmlType.ELEMENT, required=True)
    )


@dataclass
class ManyNamesElement:
    english_name: str = field(
        default=None, metadata=dict(name="NAME_EN", type=XmlType.ELEMENT, required=True)
    )
    japanese_name: str = field(
        default=None, metadata=dict(name="NAME_JP", type=XmlType.ELEMENT, required=True)
    )
    romaji_name: str = field(
        default=None, metadata=dict(name="NAME_R", type=XmlType.ELEMENT, required=True)
    )
    other_names: list[str] = field(
        default_factory=list,
        metadata=dict(name="NAME_ALT", type=XmlType.ELEMENT, min_occurs=0),
    )

    @property
    def names(self) -> Iterator[str]:
        if name := self.japanese_name:
            yield name
        if name := self.romaji_name:
            yield name
        if name := self.english_name:
            yield name
        for name in self.other_names:
            if name:
                yield name
