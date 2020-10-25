from typing import Type, Union

from lxml.etree import tostring
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.parsers.config import ParserConfig

parse = XmlParser(config=ParserConfig(fail_on_unknown_properties=False)).from_bytes


def parse_to_object(xml: Union[str, bytes], class_: Type):
    return parse(tostring(xml), class_)
