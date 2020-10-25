from abc import abstractmethod
from typing import ClassVar
from urllib.parse import urljoin

from httpx import Response, StatusCode
from lxml.etree import XMLSyntaxError, fromstring

from ..configuration import API, HOST_NAME
from ..action.abstract_paginated import Parameter
from .enum import Error


class Client:
    API = API

    # lxml do not like unicode declaration.
    DECLARATION = """<?xml version="1.0" encoding="UTF-8"?>\n"""

    @abstractmethod
    def query(self, **kwargs):
        ...

    @classmethod
    def _parse(cls, r: Response):
        if (status := r.status_code) != StatusCode.OK:
            raise Exception(f"Invalid status: {status}")

        xml = r.text.removeprefix(cls.DECLARATION)
        try:
            xml = fromstring(xml)
        except XMLSyntaxError:
            raise Exception(f"Invalid content: {xml}")

        error = xml[0]
        if error.tag == "ERROR":
            raise Error(error.attrib["code"]).error()

        return xml
