from warnings import catch_warnings, filterwarnings, simplefilter

from xsdata.exceptions import ConverterWarning
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.parsers.config import ParserConfig
from xsdata.formats.dataclass.parsers.nodes import ParserError

PARSER = XmlParser(config=ParserConfig(fail_on_unknown_properties=True)).from_string


def parse(cls, xml: str):
    try:
        with catch_warnings():
            filterwarnings("ignore", category=ConverterWarning)
            simplefilter("ignore")
            return PARSER(xml, cls)
    except ParserError as e:
        raise TypeError(f"{e} in \n{xml}") from e
