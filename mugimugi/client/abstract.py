from abc import abstractmethod
from lxml.etree import fromstring

from .enum import Error
from ..configuration import API


class Client:
    API = API

    # lxml do not like unicode declaration.
    DECLARATION = """<?xml version="1.0" encoding="UTF-8"?>\n"""
    DECLARATION_LENGTH = len(DECLARATION)

    @abstractmethod
    def query(self, **kwargs):
        ...

    @classmethod
    def _parse(cls, xml: str):
        if xml.startswith(cls.DECLARATION):
            xml = xml[cls.DECLARATION_LENGTH :]
        xml = fromstring(xml)

        error = xml[0]
        if error.tag == "ERROR":
            raise Error(error.attrib["code"]).error()

        return xml
