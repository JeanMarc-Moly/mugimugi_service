from abc import ABC
from enum import Enum
from typing import Iterator, Optional, Union

from ..configuration import RESPONSE_MAX_COUNT
from .abstract import AbstractAction, AsyncClient


class AbstractPaginatedAction(AbstractAction, ABC):
    class Parameter(Enum):
        PAGE = "page"  # int > 0

    page: Optional[int] = None

    @property
    def page_size(self) -> int:
        return RESPONSE_MAX_COUNT

    def params(self) -> Iterator[tuple[str, Union[str, int]]]:
        yield from super().params()
        yield self.Parameter.PAGE.value, self.page

    def query_many(self, client: AsyncClient, blind: bool = True):
        if blind:
            self.query_many_blind(client)
        else:
            self.query_many_smart(client)

    async def query_many_blind(self, client: AsyncClient):
        current, swap = 0, self.page

        while True:
            self.page = current = current + 1
            query = self.get_query(client)
            self.page = swap

            result = self.send_and_parse(query)
            yield result

    async def query_many_smart(self, client: AsyncClient):
        current, swap = 0, self.page
        count = max_ = self.page_size

        while count == max_:
            self.page = current = current + 1
            query = self.get_query(client)
            self.page = swap

            result = self.send_and_parse(client, query)
            yield result
            count = len((await result).elements)
