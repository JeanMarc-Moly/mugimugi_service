from typing import AsyncIterator, ClassVar, Iterable, Optional, Union
from urllib.parse import urljoin

from httpx import AsyncClient, Response, StatusCode
from lxml.etree import XMLSyntaxError, fromstring

from ..action import AbstractAction
from ..action.abstract_paginated import Parameter
from ..configuration import HOST_NAME
from .enum import Error
from .enum.item import ItemType


class Client:
    HOST_NAME = "https://www.doujinshi.org/"
    API_PATH = "api/"

    # lxml do not like unicode declaration.
    DECLARATION = """<?xml version="1.0" encoding="UTF-8"?>\n"""

    PAGE: ClassVar[str] = Parameter.PAGE.value

    # Contrary to doc, returns up to 50 elements, not 25 (+1 for user).
    MIN_PER_PAGE: ClassVar[int] = 1
    MAX_PER_PAGE: ClassVar[int] = 50 + 1

    def __init__(self, key: str) -> None:
        # 404 if no final "/"
        self.api = urljoin(urljoin(HOST_NAME, self.API_PATH), key) + "/"

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

    async def query(self, params: dict[str, Union[str, int]]):
        async with AsyncClient() as client:
            return self._parse(await client.get(self.api, params=params, timeout=None))

    async def fetch_all(self, action: AbstractAction):
        min = self.MIN_PER_PAGE
        max = self.MAX_PER_PAGE
        page = self.PAGE

        params = action.params
        params[page] = p = 1

        while min < len(xml := await self.query(params)) <= max:
            yield xml
            params[page] = p = p + 1

    async def fetch_all_elements(
        self,
        action: AbstractAction,
        include: Optional[Iterable[ItemType]] = None,
        exclude: Optional[Iterable[ItemType]] = (ItemType.USER,),
        limit: Optional[int] = None,
    ) -> AsyncIterator:
        if include:
            include = {t.value for t in include}
        exclude = {t.value for t in exclude} if exclude else []

        async for xml in self.fetch_all(action):
            for child in xml.iterchildren(include):
                if child.tag not in exclude:
                    yield child
                    if limit and not (limit := limit - 1):
                        return

    async def fetch_elements(
        self,
        action: AbstractAction,
        include: Optional[Iterable[ItemType]] = None,
        exclude: Optional[Iterable[ItemType]] = (ItemType.USER,),
    ) -> AsyncIterator:
        if include:
            include = {t.value for t in include}
        exclude = {t.value for t in exclude} if exclude else []

        for child in (await self.query(action.params)).iterchildren(include):
            if child.tag not in exclude:
                yield child
