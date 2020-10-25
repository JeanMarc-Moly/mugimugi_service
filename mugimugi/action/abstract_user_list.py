from typing import Iterable

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

    def __init__(self, books: Iterable[int]):
        self.books = set(books)

    @property
    def params(self):
        p = self.BOOK_ID_PREFIX
        params = super().params
        params[Parameter.ID.value] = self.CONTENT_SEPARATOR.join(
            p + str(b) for b in self.books
        )
        return params

    @classmethod
    def get_from_typed_id(cls, books: Iterable[str]):
        return cls(int(b[1:] for b in books))
