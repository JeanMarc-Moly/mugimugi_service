from enum import Enum
from typing import Iterator, Optional, Union

from ..configuration import RESPONSE_MAX_COUNT
from .abstract import AbstractAction


class Parameter(Enum):
    PAGE = "page"  # int > 0


class AbstractPaginatedAction(AbstractAction):
    PAGE_SIZE = RESPONSE_MAX_COUNT
    page: Optional[int] = None

    def __iter__(self) -> Iterator[Iterator[tuple[str, Union[str, int]]]]:
        self.page = 0
        max = self.PAGE_SIZE
        while len((yield self).elements) == max:
            self.page += 1

    def items(self) -> Iterator[tuple[str, Union[str, int]]]:
        yield from super().items()
        yield Parameter.PAGE.value, self.page
