from abc import abstractmethod
from http import HTTPStatus
from httpx import Response
from lxml.etree import fromstring, XMLSyntaxError

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
    def _parse(cls, r: Response):
        if (status := r.status_code) != HTTPStatus.OK:
            raise Exception(f"Invalid status: {status}")

        xml = r.text
        if xml.startswith(cls.DECLARATION):
            xml = xml[cls.DECLARATION_LENGTH :]

        try:
            xml = fromstring(xml)
        except XMLSyntaxError:
            raise Exception(f"Invalid content: {xml}")

        error = xml[0]
        if error.tag == "ERROR":
            raise Error(error.attrib["code"]).error()

        return xml
