from abc import ABC
from dataclasses import dataclass, field
from typing import Generic, Iterator, TypeVar
from warnings import catch_warnings, filterwarnings, simplefilter

from xsdata.exceptions import ConverterWarning
from xsdata.formats.dataclass.models.elements import XmlType
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.parsers.config import ParserConfig
from xsdata.formats.dataclass.parsers.nodes import ParserError

from ..enum import ElementNode
from .error import Error
from .user import User

PARSER = XmlParser(config=ParserConfig(fail_on_unknown_properties=True)).from_string


def parse(cls, xml: str):
    try:
        with catch_warnings():
            filterwarnings("ignore", category=ConverterWarning)
            simplefilter("ignore")
            return PARSER(xml, cls)
    except ParserError as e:
        raise TypeError(f"Failed to parse: {e}")


@dataclass
class AbstractRoot(ABC):
    class Meta:
        name = ElementNode.LIST.value

    @classmethod
    def parse(cls, xml: str):
        return parse(cls, xml)


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
