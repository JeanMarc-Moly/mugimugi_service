from typing import Iterable, Optional

from .abstract import AsynchronousClient
from ..abstract_paginated import PaginatedClient
from ..enum import ItemType


class AsynchronousPaginatedClient(AsynchronousClient, PaginatedClient):
    async def fetch_all(self, **kwargs):
        min = self.MIN_PER_PAGE
        max = self.MAX_PER_PAGE

        params = self.params | kwargs
        params[self.PAGE] = p = 1

        while min < len(xml := await self._query(params)) <= max:
            yield xml
            params[self.PAGE] = p = p + 1

    async def fetch_all_elements(
        self,
        include: Optional[Iterable[ItemType]] = None,
        exclude: Optional[Iterable[ItemType]] = (ItemType.USER,),
        **kwargs,
    ):
        if include:
            include = {t.value for t in include}
        exclude = {t.value for t in exclude} if exclude else []

        async for xml in self.fetch_all(**kwargs):
            childrens = xml.iterchildren(include)
            for child in childrens:
                if child.tag not in exclude:
                    yield child
