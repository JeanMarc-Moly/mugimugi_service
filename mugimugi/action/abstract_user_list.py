from typing import Iterable, Union

from fast_enum import FastEnum

from ..enum import ItemType
from .abstract import AbstractAction


class Parameter(metaclass=FastEnum):
    ID = "ID"


class AbstractUserListAction(AbstractAction):
    CONTENT_SEPARATOR = ","
    # Beyond this count, books are ignoerd.
    MAX_COUNT_OF_BOOK = 25
    BOOK_ID_PREFIX = ItemType.BOOK.value

    def __init__(self, books: Iterable[Union[str, int]], split_list=False):
        p = self.BOOK_ID_PREFIX
        self.books = {b if b.startswith(p) else p + b for b in (str(b) for b in books)}
        self.split_list = split_list

    @property
    def params(self):
        params = super().params
        params[Parameter.ID.value] = self.CONTENT_SEPARATOR.join(self.books)
        return params
